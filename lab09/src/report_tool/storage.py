import pathlib

def save_report(report_text: str, filename: str) -> str:
    path = pathlib.Path(f"{filename}.txt")
    path.write_text(report_text, encoding="utf-8")
    return str(path.absolute())

def read_back(filepath: str) -> str:
    path = pathlib.Path(filepath)
    if path.exists():
        return path.read_text(encoding="utf-8")
    return "File not found."

if __name__ == "__main__":
    print("Module: storage")
    print("Public API: save_report, read_back")
    print("Usage example:")
    test_path = save_report("Test Content", "test_doc")
    print(f"File saved at: {test_path}")
    print(f"Content: {read_back(test_path)}")