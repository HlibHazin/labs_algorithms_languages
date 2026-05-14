# 🐍 Lab 12: Testing an Async CLI Tool

## 🎯 Goal
The goal is to understand:
- how to test async functions 
- how to test CLI applications 
- the difference between unit and behavior tests
## 📂 Project Structure


```
lab12/
├── README.md              
├── requirements.txt    
├── report/                
│   └── answers.md
├── src/             
│   └── async_tool/
│       └── __main__.py
└── tests/
    ├── test_cli.py
    └── test_process_item.py

```

## 💻 Install dependencies
Ensure you have the required testing frameworks installed (pytest and pytest-asyncio).
```bash
pip install pytest pytest-asyncio
```
---

## ⚙️ Testing Scope

The test suite is divided into two main parts to ensure overall stability:

* **Part A: Unit Tests (`test_process_item.py`):** Directly tests the `process_item` coroutine using `pytest.mark.asyncio`. Validates successful execution, proper error handling (raising `ValueError`), and the correct structure of the returned dictionary.
* **Part B: Behavior Tests (`test_cli.py`):** Tests the application from the end-user's perspective using the `subprocess` module. It creates temporary `input.json` files and verifies exit codes, JSON output validity, concurrent mode behavior, and error handling via CLI flags without modifying the internal code.

---

## 🚀 Usage Examples

### Example 1: Run all tests
Runs the entire test suite (both unit and behavior tests) with verbose output.

```bash
python -m pytest -v
```

### Example 2: Run only Unit Tests
Executes only the isolated tests for the async function.

```bash
python -m pytest tests/test_process_item.py -v
```

### Example 3: Run only Behavior (CLI) Tests
Executes only the black-box tests that interact with the CLI application.

```bash
python -m pytest tests/test_cli.py -v
```
---