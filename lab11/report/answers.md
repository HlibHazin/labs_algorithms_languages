# Lab 11: Async Batch Processor - Answers

**1. Why does `await` inside a loop lead to sequential execution?**

`await` pauses the execution of the current function until the awaited coroutine finishes. In a `for` loop, the loop cannot proceed to the next iteration to start the next task until the current `await` resolves, creating a strict one-by-one sequence.

**2. How does `asyncio.gather` change behavior?**

Instead of waiting for tasks one by one, `asyncio.gather` schedules multiple tasks to run concurrently (at the same time) on the event loop. It waits for all of them to complete and returns their results in the original order.

**3. What happens if one task fails in async mode without `--continue-on-error`?**

If any task raises an exception, `asyncio.gather` immediately propagates that exception to the caller. The program will crash and exit with a non-zero code, halting further execution, even if other tasks were running successfully.

**4. Why is semaphore needed?**

A semaphore restricts the maximum number of tasks that can run simultaneously. This prevents resource exhaustion (like running out of memory, hitting API rate limits, or opening too many database connections) when processing thousands of concurrent tasks.

**5. When should async NOT be used?**

Async should NOT be used for CPU-bound tasks (e.g., heavy mathematical computations, image processing). Python's Global Interpreter Lock (GIL) prevents true thread parallelism for CPU operations, meaning async will not provide a speedup and the event loop will be blocked. `multiprocessing` is the correct choice for CPU-bound work.