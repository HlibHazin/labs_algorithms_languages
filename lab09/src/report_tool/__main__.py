from .helpers import parse_numbers, analyze_numbers
from .formatting import build_sorted_report
from .storage import save_report, read_back

def _show_help():
    print("Report Tool - A simple utility for parsing and analyzing numeric reports.")
    print("Main capabilities: Parse numbers, calculate statistics, generate reports, and save them.")
    print("\nUsage example:")
    print("  python -m report_tool")
    print("\nExample string input: '4, 8, 15, 16, 23, 42'\n")

def _example_workflow():
    text = "4, 8, 15, 16, 23, 42"
    numbers = parse_numbers(text)
    stats = analyze_numbers(numbers)
    report = build_sorted_report(numbers, stats)
    return report

def main():
    _show_help()
    print("=" * 30)
    report = _example_workflow()
    print("Generated Report:")
    print(report)

    path = save_report(report, "report_output")
    print(f"\nSaved to: {path}")
    print("\nSaved file content:")
    print(read_back(str(path)))

if __name__ == "__main__":
    main()