# 🐍 Lab 02: Expressions & Control Flow in Python

## 🎯 Goal
The goal of this lab is to practice Python expressions and control flow while demonstrating an understanding of truthiness, identity vs equality, modern control flow (match), comprehensions, and lazy evaluation.

---

## 📂 Project Structure


```
LABS/                       
│
├── .gitignore                              
│
└── lab02/    
    │              
    ├── README.md      
    │
    ├── requirements.txt
    │
    ├── report/                  
    │   └── answers.md        
    │
    └── src/              
        └── lab02.py       
```
---

## 💻 Environment Setup

All commands must be executed from the project root directory.

### 1. Create virtual environment

```bash
python -m venv .venv
```

### 2. Activate virtual environment

#### Windows
```bash
.venv\Scripts\activate
```

#### macOS / Linux
```bash
source .venv/bin/activate
```

After activation, the terminal should display:

```
(.venv)
```

### 3. Install dependencies

```bash
pip install -r lab02/requirements.txt
```

This project uses only the Python standard library.

---

## 🚀 Run the Program

```bash
python lab02/src/lab02.py
```

---


## 🔍 Program Output Overview

The program prints six clearly labeled sections (A–F).  
Each section demonstrates a specific Python concept.

---


### A) Truthiness

Demonstrates:

- How Python evaluates the boolean value of different objects like 0, [], None, etc.

Shows that:

- Python treats empty containers as False.
- Truthiness is an inherent property of objects used in conditional logic.

---

### B) Identify vs Equality

Demonstrates:

- The difference between value comparison (==) and object identity (is)

Shows that:

- == checks if two objects have equal values.
- is checks if two names are bound to the exact same object in memory.
- Immutable objects (like strings) may exhibit special "interning" behavior.

---

### C) Control Flow

Demonstrates:

- Implementation of describe_number(x) using if-elif logic .

Shows that:

- Conditional branches can categorize numeric data into specific ranges .
- Order of evaluation in if-elif is crucial for correct logic.

---

### D) Pattern Matching

Demonstrates:

- Processing structured event tuples (click, keypress, quit) using match .
  
Shows that:

- match provides a convenient way to deconstruct and analyze complex data structures.
  
---

### E) Comprehensions

Demonstrates:

- Creating lists and dictionaries using concise syntax .
  
Shows that:

- List comprehensions can replace simple loops for generating collections.
- Conditional logic (filtering) can be embedded directly within the comprehension.

---

### F) Generators

Demonstrates:

- A generator function even_numbers(limit) and generator expressions .
  
Shows that:

- Generators are "lazy" — they produce values one-by-one only when requested.
- They allow processing large datasets (like 1,000,000 items) without high memory overhead .
---

