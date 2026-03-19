# 🐍 Lab 03: Functions as Objects, Lambda, Closures

## 🎯 Goal
The goal of this lab is to explore Python functions as first-class objects and understand how functions can: 1) be assigned to variables, 2) be passed as arguments, 3) be created dynamically, 4) capture variables from their environment (closures).

---

## 📂 Project Structure


```
LABS/                       
│
├── .gitignore                              
│
└── lab03/    
    │              
    ├── README.md      
    │
    ├── requirements.txt
    │
    ├── report/                  
    │   └── answers.md        
    │
    └── src/              
        └── lab03.py       
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
pip install -r lab03/requirements.txt
```

This project uses only the Python standard library.

---

## 🚀 Run the Program

```bash
python lab03/src/lab03.py
```

---


## 🔍 Program Output Overview

The program prints six clearly labeled sections (A–F).  
Each section demonstrates a specific Python concept.

---


### A) Functions as Objects

Demonstrates:

- Implementation of apply_twice(func, x) which takes a function as a first-class object.
- Passing both named functions (like abs) and anonymous lambda expressions as arguments.

Shows that:

- Functions in Python can be treated like any other variable or object.
- Higher-order functions can abstract logic by accepting other functions as data.

---

### B) Sorting with Lambda

Demonstrates:

- Sorting a list of tuples (name, age) using the built-in sorted() function .
- Using lambda expressions as the key argument to extract specific elements for comparison.

Shows that:

- lambda provides a concise way to define one-time-use functions for data transformation.
- Complex data structures can be easily reordered based on internal attributes.
  
---

### C) Function Factory

Demonstrates:

- A function make_multiplier(k) that dynamically creates and returns a new function.
- Generating specialized functions like times3 at runtime.

Shows that:

- Python functions can return other functions, enabling functional "factories".
- The returned function remembers the value of k from its parent's scope.

---

### D) Closure Counter

Demonstrates:

- Implementing a stateful counter() using a nested function and a closure.
- Using the nonlocal keyword to modify a variable in the outer (enclosing) scope.
  
Shows that:

- Closures allow a function to "capture" and persist an internal state without using global variables.
- Each call to the counter factory creates a unique, isolated environment .
  
---

### E) Lambda vs def

Demonstrates:

- Two equivalent implementations of a squaring function: one using the standard def and another using lambda .
- Execution of both to prove identical behavior.
  
Shows that:

- lambda is syntactically restricted to a single expression but functionally identical to simple def functions.
- The choice between them usually depends on the need for reuse versus brevity.

---

### F) Functional Composition

Demonstrates:

- A data processing pipeline using sum(), lambda, and generator expressions.
- Sequential steps: filtering even numbers and squaring them in a single line.

Shows that:

- Generator expressions provide memory-efficient ways to process sequences.
- Combining multiple functional tools allows for clean, declarative code for mathematical operations.

