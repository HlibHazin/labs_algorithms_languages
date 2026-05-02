from .helpers import _sort_numbers

def _line_maker(name: str, value) -> str:
    return f"{name}: {value}"

def _pretty_title(text: str) -> str:
    return text.strip().title()

def _internal_banner() -> str:
    return "=" * 30

def build_report(stats: dict) -> str:
    lines = []
    lines.append(_pretty_title("number report"))
    lines.append("-" * 20)
    lines.append(_line_maker("count", stats["count"]))
    lines.append(_line_maker("sum", stats["sum"]))
    lines.append(_line_maker("min", stats["min"]))
    lines.append(_line_maker("max", stats["max"]))
    lines.append(_line_maker("mean", round(stats["mean"], 2)))
    return "\n".join(lines)

def build_sorted_report(numbers: list[float], stats: dict) -> str:
    ordered = _sort_numbers(numbers)
    lines = []
    lines.append(_pretty_title("number report"))
    lines.append("-" * 20)
    lines.append(_line_maker("count", stats["count"]))
    lines.append(_line_maker("sum", stats["sum"]))
    lines.append(_line_maker("min", stats["min"]))
    lines.append(_line_maker("max", stats["max"]))
    lines.append(_line_maker("mean", round(stats["mean"], 2)))
    lines.append(_line_maker("sorted", ordered))
    return "\n".join(lines)

if __name__ == "__main__":
    print("Module: formatting")
    print("Public API: build_report, build_sorted_report")
    print("Usage example:")
    sample_stats = {"count": 3, "sum": 12, "min": 2, "max": 6, "mean": 4.0}
    print(build_report(sample_stats))