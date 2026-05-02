import argparse
import logging
from pathlib import Path
import json

from .helpers import parse_numbers, analyze_numbers
from .formatting import build_sorted_report
from .storage import save_report

def setup_logging(level_name: str):
    """Configure the logger with the specified level"""
    numeric_level = getattr(logging, level_name.upper(), None)
    if not isinstance(numeric_level, int):
        raise ValueError(f"Invalid log level: {level_name}")
    
    logging.basicConfig(
        level=numeric_level,
        format='%(asctime)s - %(levelname)s - %(message)s'
    )

def main():
    parser = argparse.ArgumentParser(description="Report Tool CLI - parses and analyzes numeric data.")
    
    parser.add_argument("--input", required=True, help="Path to the input file containing numbers")
    parser.add_argument("--out", required=True, help="Path to save the generated report")
    parser.add_argument("--format", choices=["text", "json"], required=True, help="Output format: 'text' or 'json'")
    parser.add_argument("--log-level", choices=["DEBUG", "INFO", "WARNING", "ERROR"], default="INFO", help="Set the logging level")
    
    args = parser.parse_args()

    setup_logging(args.log_level)
    logger = logging.getLogger(__name__)

    logger.info("Starting Report Tool pipeline.")

    try:
        input_path = Path(args.input)
        logger.debug(f"Attempting to read input file: {input_path}")
        
        if not input_path.exists():
             logger.error(f"Input file not found: {input_path}")
             return

        raw_text = input_path.read_text(encoding="utf-8")
        logger.info(f"Successfully read {len(raw_text)} characters from {input_path.name}")

        logger.debug("Parsing numbers from text...")
        numbers = parse_numbers(raw_text)
        
        logger.debug("Analyzing parsed numbers...")
        stats = analyze_numbers(numbers)

        output_path = Path(args.out)
        
        if args.format == "text":
            logger.debug("Formatting output as plain text...")
            report_content = build_sorted_report(numbers, stats)
            
            logger.debug(f"Writing text report to {output_path}")
            output_path.write_text(report_content, encoding="utf-8")
            
        elif args.format == "json":
            logger.debug("Formatting output as JSON...")
            json_data = {
                "original_numbers": numbers,
                "statistics": stats
            }
            report_content = json.dumps(json_data, indent=4)
            
            logger.debug(f"Writing JSON report to {output_path}")
            output_path.write_text(report_content, encoding="utf-8")

        logger.info(f"Success! Report saved to {output_path.absolute()}")

    except ValueError as ve:
         logger.error(f"Data error: {ve}")
    except Exception as e:
        logger.error(f"An unexpected error occurred: {e}", exc_info=True)

if __name__ == "__main__":
    main()