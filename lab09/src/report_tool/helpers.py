def _cleanup_pieces(parts: list[str]) -> list[str]:
    cleaned = []
    for item in parts:
        item = item.strip()
        if item != "":
            cleaned.append(item)
    return cleaned

def _check_input(numbers: list[float]):
    if not numbers:
        raise ValueError("numbers must not be empty")

def _sort_numbers(numbers: list[float]) -> list[float]:
    return sorted(numbers)

def parse_numbers(text: str) -> list[float]:
    pieces = text.replace(";", ",").split(",")
    pieces = _cleanup_pieces(pieces)
    result = []
    for p in pieces:
        result.append(float(p))
    return result

def analyze_numbers(numbers: list[float]) -> dict:
    _check_input(numbers)
    total = sum(numbers)
    count = len(numbers)
    avg = total / count
    return {
        "count": count,
        "sum": total,
        "min": min(numbers),
        "max": max(numbers),
        "mean": avg,
    }

if __name__ == "__main__":
    print("Module: helpers")
    print("Public API: parse_numbers, analyze_numbers")
    print("Usage example:")
    nums = parse_numbers("1, 2.5, 3")
    print(f"Parsed: {nums}")
    print(f"Stats: {analyze_numbers(nums)}")