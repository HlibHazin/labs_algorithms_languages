# 🐍 Lab 09: Repairing a Broken Python Project

## 🎯 Goal
Transform the given project into a clean, structured, and usable Python tool.

## 📂 Project Structure


```
lab09/
├── README.md              
├── requirements.txt       
├── report/                
│   └── report.md
└── src/                
    └── report_tool/
        ├── __init__.py
        ├── __main__.py
        ├── formatting.py
        ├── helpers.py
        └── storage.py

```

## 💻 Install dependencies

```bash
pip install -r lab09/requirements.txt
```
---

## 🚀 Run the Program

### Run the entire tool as a package:

```bash
cd lab09/src
python -m report_tool
```
### Run individual modules to see their usage:

```bash
cd lab09/src
python -m report_tool.formatting
python -m report_tool.helpers
python -m report_tool.storage
```

---

## 🔍 Program Output Overview

### A) Task A: Clean Project Shape

Demonstrates:

- Reorganizing the code into a proper package structure (src/report_tool/).
- Cleaning requirements.txt to reflect zero external dependencies.

Shows that:

- A clean project shape significantly improves maintainability. Moving debug code inside if __name__ == "__main__": blocks prevents unintended side-effects when modules are imported elsewhere.

---

### B) Task B: Public vs Private Design

Demonstrates:

- Marking internal helper functions with an underscore prefix (e.g., _check_input, _sort_numbers).
- Ensuring only essential functions are exposed for external use.

Shows that:

- Python uses conventions (the _ prefix) to signal that a function is internal logic. This creates a safer and more predictable API for end-users. 

---

### C) Task C: Execution Behavior

Demonstrates:

- Executing python -m report_tool triggers the __main__.py file, outputting tool capabilities, usage instructions, and a generated sample report.
- Executing individual modules (e.g., python -m report_tool.helpers) outputs specific module purposes and minimal usage examples.

Shows that:

- A well-designed package handles execution context gracefully. It acts as a usable application when called via -m, but remains a silent, safe library when imported.


---

### D & E) Task D & E: Package-level API & Stable Usage

Demonstrates:

- Utilizing the __init__.py file to explicitly define __all__ exports.
- Allowing direct imports from the root package: from report_tool import parse_numbers, build_report.

Shows that:

- Users do not need to memorize the internal file structure. They can interact with a unified, stable API at the package level without relying on path hacks.