# 🐍 Lab 11: Async Batch Processor

## 🎯 Goal
Implement a CLI tool that processes a batch of tasks in different execution modes:
- sequential (sync) 
- concurrent (async) 
- limited concurrency (semaphore) 

## 📂 Project Structure


```
lab11/
├── README.md              
├── requirements.txt 
├── input.json      
├── report/                
│   └── answers.md
└── src/             
    └── async_tool/
        └── __main__.py
        

```

## 💻 Install dependencies

```bash
pip install -r lab11/requirements.txt
```
---

## ⚙️ Supported CLI Arguments

The tool is executed as a Python module and requires specific arguments to run:

* `input` : **(Required)** Path to the input JSON file containing the task list.
* `--mode <sync|async|limited>` : *(Optional)* Execution mode. Default is `sync`.
* `--limit <N>` : *(Optional)* Concurrency limit (used only in `limited` mode). Default is `5`.
* `--continue-on-error` : *(Optional)* If provided, the program catches task failures, records them, and continues processing the remaining tasks.
* `--log-level <DEBUG|INFO|WARNING|ERROR>` : *(Optional)* Sets the verbosity of the logging output. Default is `WARNING`.

---

## 📄 Output Format

* **json**: The program outputs a structured, machine-readable JSON array of results directly to the standard output (`stdout`). Logs are safely directed to `stderr` to prevent corrupting the JSON output.

---

## 🚀 Usage Examples

### Example 1: Sequential Mode (sync)
Runs tasks strictly one by one. If an error occurs (and `--continue-on-error` is not set), the program aborts.

```bash
python -m src.async_tool input.json --log-level INFO
```

### Example 2: Concurrent Mode (async)
Runs all tasks simultaneously. Uses the continue flag to ensure the program finishes and outputs the JSON even if a task fails.

```bash
python -m src.async_tool input.json --mode async --continue-on-error --log-level INFO
```

### Example 3: Limited Concurrency Mode (limited)
Runs tasks concurrently, but strictly limits the number of active tasks at any given moment to 2 using a Semaphore.

```bash
python -m src.async_tool input.json --mode limited --limit 2 --continue-on-error --log-level INFO
```
## 🚀 Run mypy --strict

```bash
mypy --strict src/async_tool/__main__.py
```
