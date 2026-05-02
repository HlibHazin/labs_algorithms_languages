# 🐍 Lab 10: Turning a Python Package into a CLI Tool

## 🎯 Goal

Extend your existing report_tool so that it can be used as a real command-line tool that:
- reads input data from files, 
- processes it using your existing logic, 
- produces output in different formats, 
- provides controlled logging of its execution.
  
The focus of this lab is on:
- CLI design (argparse) 
- file handling (pathlib) 
- structured data (json) 
- logging (logging) 
- integration with an existing codebase  
## 📂 Project Structure


```
lab10/
├── README.md              
├── requirements.txt       
├── report/                
│   └── report.md
└── src/
    ├── data.txt               
    └── report_tool/
        ├── __init__.py
        ├── __main__.py
        ├── formatting.py
        ├── helpers.py
        └── storage.py

```

## 💻 Install dependencies

```bash
pip install -r lab10/requirements.txt
```
---

## ⚙️ Supported CLI Arguments

The tool is executed as a Python module and requires specific arguments to run dynamically:

* `--input <file>` : **(Required)** Path to the text file containing the input numbers.
* `--out <file>` : **(Required)** Path where the generated report will be saved.
* `--format <text|json>` : **(Required)** The output format of the report.
* `--log-level <DEBUG|INFO|WARNING|ERROR>` : *(Optional)* Sets the verbosity of the logging output. Default is `INFO`.

---

## 📄 Supported Output Formats

* **text**: Generates a human-readable summary report with a title and aligned data fields.
* **json**: Generates a structured, machine-readable JSON file containing the original parsed numbers and the calculated statistics.

---

## 🚀 Usage Examples

*Note: Ensure you are in the `src/` directory where your `data.txt` is located before running the commands.*

### Example 1: Generating a Text Report (Standard usage)
Reads data, calculates statistics, saves a human-readable text file, and shows standard `INFO` logs.

```bash
cd lab10/src
python -m report_tool --input data.txt --out report.txt --format text --log-level INFO
```

### Example 2: Generating a JSON Report (Silent/Automated usage)
Reads data, calculates statistics, saves a structured JSON file, and suppresses normal output to only show `WARNING` or `ERROR` logs.

```bash
cd lab10/src
python -m report_tool --input data.txt --out report.json --format json --log-level WARNING
```