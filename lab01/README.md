# LAB01 — Names & Objects (Binding), Mutability, Copy, GC (CPython)

## Description

This laboratory demonstrates fundamental Python concepts related to:

- Names and object bindings
- Rebinding vs mutation
- Function argument behavior
- Default mutable arguments
- Shallow vs deep copy
- Reference counting and garbage collection in CPython

The goal of this lab is to observe and explain object behavior rather than implement complex algorithms.

---

## Project Structure

```
LABS/                       
│
├── .gitignore                              
│
└── lab01/    
    │              
    ├── README.md      
    │
    ├── requirements.txt
    │
    ├── report/                  
    │   └── answers.md        
    │
    └── src/              
        └── lab01.py       
```

---

## Environment Setup

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
pip install -r requirements.txt
```

This project uses only the Python standard library.

---

## Run the Program

```bash
python lab01/src/lab01.py
```

---

## Program Output Overview

The program prints six clearly labeled sections (A–F).  
Each section demonstrates a specific Python concept.

---

### A) Binding / Rebinding

Demonstrates:

- Two names bound to the same object
- Rebinding one name
- Object identity using `id()`

Shows that:

- Names in Python are bindings
- Rebinding changes the name–object relationship
- Objects themselves are not modified

---

### B) Mutation vs Rebinding

Demonstrates:

- Two names referencing the same list
- Mutation of the object through one name

Shows that:

- Mutation modifies the object in place
- Both names observe the change
- `id(a) == id(b)` remains True after mutation

---

### C) Function Arguments

Demonstrates:

- A function that mutates a list
- A function that rebinds its parameter

Shows that:

- Mutation inside a function affects the caller
- Rebinding inside a function does not affect the caller
- Parameters are new local names
- Argument passing is binding, not copying

---

### D) Default Argument Behavior

Demonstrates:

- A function with a mutable default argument
- Multiple calls to that function

Shows that:

- Default values are evaluated once
- The same object is reused across calls
- The list keeps growing because the same object is modified

---

### E) Copy Semantics (Shallow vs Deep Copy)

Demonstrates:

- Copying a nested list using `.copy()`
- Copying using `copy.deepcopy()`

Shows that:

- A shallow copy creates a new outer container
- Nested objects remain shared
- A deep copy duplicates nested objects recursively

---

### F) Reference Counting / GC (CPython)

Demonstrates:

- Reference counting using `sys.getrefcount()`
- Increased reference count after creating another binding
- Special behavior of small integers

Shows that:

- Reference count increases when a new binding is created
- Small integers may display unusual reference counts
- This is due to CPython optimization
- Small integers are immortal objects
- This behavior is an implementation detail and is not guaranteed by the Python language specification

---