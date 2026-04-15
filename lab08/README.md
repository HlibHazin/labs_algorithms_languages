# 🐍 Lab 08: Iteration, Context Managers, and Descriptors

## 🎯 Goal
The goal is to understand that Python behavior is driven by protocols implemented via special methods.

## 📂 Project Structure


```
lab08/
├── README.md              
├── requirements.txt       
├── report/                
│   └── answers.md
└── src/                   
    └── lab08.py
```
---

## 💻 Install dependencies

```bash
pip install -r lab08/requirements.txt
```
---

## 🚀 Run the Program

```bash
python lab08/src/lab08.py
```

---

---

## 🚀 Run mypy --strict

```bash
mypy --strict lab08/src/lab08.py
```

---

## 🔍 Program Output Overview

The program prints four clearly labeled sections (A–D), plus a static type checking verification. Each section demonstrates a specific concept of the Python Data Model related to core protocols and advanced attribute management.

---

### A) Task A: Iteration

Demonstrates:

- Instantiating a `StudentCollection` and iterating over its students using a standard `for` loop.
- The underlying interaction between the collection and a custom `StudentIterator` class.

Shows that:

- Python natively supports custom iteration logic through the Iterator Protocol.
- By implementing the `__iter__()` and `__next__()` magic methods, any custom object can seamlessly integrate with Python's iteration mechanisms without relying on manual, index-based loops.

---

### B) Task B: Context Manager

Demonstrates:

- Wrapping the `StudentCollection` usage within a `with` statement block.
- Printing explicit entry and exit messages that map to the lifecycle of the context.

Shows that:

- The Context Manager protocol allows objects to cleanly manage setup and teardown logic.
- By implementing the `__enter__()` and `__exit__()` methods, the object guarantees that actions (like resource cleanup) are properly executed upon exiting the block, even if an unexpected error or exception occurs inside the loop.

---

### C) Task C: Descriptor

Demonstrates:

- Defining a `GradeDescriptor` to manage and validate access to a student's grade.
- Intentionally attempting to assign an invalid grade (e.g., 120) to a `Student` object, which successfully intercepts the action and triggers a `ValueError`.

Shows that:

- Descriptors allow developers to override and customize standard attribute access behavior.
- By using the `__get__()` and `__set__()` methods, you can enforce strict, reusable data validation rules at the class level, preventing instances from ever entering an invalid or corrupted state.

---

### D) Task D: Integration

Demonstrates:

- Combining all the implemented protocols simultaneously: entering the `StudentCollection` via a `with` statement, directly iterating over the objects, and safely accessing their descriptor-validated grades.

Shows that:

- Python’s protocol-based data model is highly composable. A single custom class can implement multiple special "dunder" methods at once, resulting in robust, expressive, and purely idiomatic Python code.