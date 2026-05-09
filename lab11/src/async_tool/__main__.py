import argparse
import asyncio
import json
import logging
import sys
from pathlib import Path
from typing import TypedDict, Any, Coroutine

class TaskItem(TypedDict):
    id: int
    delay: float
    good: bool

class TaskResult(TypedDict, total=False):
    id: int
    status: str
    message: str

async def process_item(item: TaskItem) -> TaskResult:
    await asyncio.sleep(item["delay"])
    if not item["good"]:
        raise ValueError(f"Task {item['id']} failed")
    return {
        "id": item["id"],
        "status": "done"
    }

logger = logging.getLogger(__name__)

async def safe_process(item: TaskItem, continue_on_error: bool) -> TaskResult:
    """Wrapper for handling errors of each task."""
    logger.info(f"Starting task {item['id']} (delay: {item['delay']}s)")
    try:
        result = await process_item(item)
        logger.info(f"Completed task {item['id']}")
        return result
    except Exception as e:
        logger.error(f"Task {item['id']} failed: {e}")
        if continue_on_error:
            return {
                "id": item["id"],
                "status": "error",
                "message": str(e)
            }
        raise 

async def sem_process(item: TaskItem, sem: asyncio.Semaphore, continue_on_error: bool) -> TaskResult:
    """Wrapper for limited concurrency using a Semaphore."""
    async with sem:
        return await safe_process(item, continue_on_error)

async def run_sync(tasks: list[TaskItem], continue_on_error: bool) -> list[TaskResult]:
    """Sequential mode: process tasks one by one using await in a loop."""
    results: list[TaskResult] = []
    for task in tasks:
        results.append(await safe_process(task, continue_on_error))
    return results

async def run_async(tasks: list[TaskItem], continue_on_error: bool) -> list[TaskResult]:
    """Async mode: process all tasks concurrently using asyncio.gather."""
    coros = [safe_process(t, continue_on_error) for t in tasks]
    return await asyncio.gather(*coros)

async def run_limited(tasks: list[TaskItem], limit: int, continue_on_error: bool) -> list[TaskResult]:
    """Limited mode: process tasks concurrently with a limit using a Semaphore."""
    sem = asyncio.Semaphore(limit)
    coros = [sem_process(t, sem, continue_on_error) for t in tasks]
    return await asyncio.gather(*coros)

def setup_logging(level_name: str) -> None:
    numeric_level = getattr(logging, level_name.upper(), None)
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(message)s',
        stream=sys.stderr  
    )

async def main_async() -> None:
    parser = argparse.ArgumentParser(description="Async Batch Processor")
    parser.add_argument("input", help="Path to input JSON file")
    parser.add_argument("--mode", choices=["sync", "async", "limited"], default="sync", help="Execution mode")
    parser.add_argument("--limit", type=int, default=5, help="Concurrency limit for 'limited' mode")
    parser.add_argument("--continue-on-error", action="store_true", help="Continue processing if a task fails")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="WARNING", help="Logging level")
    
    args = parser.parse_args()
    setup_logging(args.log_level)

    input_path = Path(args.input)
    if not input_path.exists():
        logger.error(f"Input file {input_path} not found")
        sys.exit(1)

    with open(input_path, "r", encoding="utf-8") as f:
        tasks: list[TaskItem] = json.load(f)

    logger.debug(f"Loaded {len(tasks)} tasks. Mode: {args.mode}")

    try:
        if args.mode == "sync":
            results = await run_sync(tasks, args.continue_on_error)
        elif args.mode == "async":
            results = await run_async(tasks, args.continue_on_error)
        else: 
            results = await run_limited(tasks, args.limit, args.continue_on_error)
            
        print(json.dumps(results, indent=2))
        
    except Exception as e:
        logger.error(f"Execution aborted due to error: {e}")
        sys.exit(1)

def main() -> None:
    asyncio.run(main_async())

if __name__ == "__main__":
    main()