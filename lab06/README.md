# 🐍 Lab 06: Python Object Model and Basic Object Behavior

## 🎯 Goal
The goal of this lab is to practice:
- working with classes and objects 
- understanding how attributes are stored 
- implementing basic dunder methods 
- controlling object behavior in Python 
- writing type-safe code with mypy --strict
---

## 📂 Project Structure


```
lab06/
├── README.md              
├── requirements.txt       
├── report/                
│   └── answers.md
└── src/                   
    └── lab06.py
```
---

## 💻 Install dependencies

```bash
pip install -r lab06/requirements.txt
```
---

## 🚀 Run the Program

```bash
python lab06/src/lab06.py
```

---

---

## 🚀 Run mypy --strict

```bash
mypy --strict lab06/src/lab06.py
```

---

## 🔍 Program Output Overview

The program prints seven clearly labeled sections (A–H). Each section demonstrates a specific concept of the Python Object Model and basic object behavior.

---

### A) Object Initialization

Demonstrates:

- Instantiating a custom `Student` object with `name`, `group`, and `average_grade` attributes.
- Accessing and printing these attributes individually using dot notation.

Shows that:

- The `__init__` method correctly intercepts the creation process to assign incoming arguments to instance variables.
- Object attributes are persistently stored in the instance and easily retrievable.

---

### B) Internal Structure (`__dict__`)

Demonstrates:

- Accessing the object's `__dict__` attribute to view its internal state as a standard dictionary.
- Modifying an attribute's value (e.g., `average_grade`) directly through this dictionary.

Shows that:

- Python objects dynamically store their mutable attributes under the hood in a dictionary format.
- Changes made directly to the `__dict__` mapping immediately alter the actual state of the object.

---

### C & D) String Representations (`__str__` and `__repr__`)

Demonstrates:

- Calling `str()` to produce a human-readable, friendly description of the student.
- Calling `repr()` to produce a formal, developer-oriented string.

Shows that:

- `__str__` customizes how an object is presented to end-users (like when using `print()`).
- `__repr__` provides an unambiguous representation meant for debugging, logging, and ideally, recreating the object.

---

### E) Object Equality (`__eq__`)

Demonstrates:

- Comparing two different `Student` objects and two identical `Student` objects using the `==` operator.
- Attempting to compare a `Student` object with an incompatible type (like a string).

Shows that:

- Defining `__eq__` overrides Python's default behavior (which compares memory addresses) to compare actual attribute values instead.
- Using `other: object` and `isinstance()` allows the method to safely handle and reject invalid comparisons without crashing the program.

---

### F & G) Ordering and Sorting (`__lt__`)

Demonstrates:

- Creating a list containing multiple `Student` objects with varying grades.
- Calling Python's built-in `students.sort()` method and iterating through the cleanly sorted list.

Shows that:

- Implementing the `__lt__` (less than) method seamlessly integrates custom classes with Python's native sorting algorithms.
- Rich comparison methods teach Python the logical rules for how your custom objects relate to one another (in this case, by `average_grade`).

---

### H) Static Type Checking (mypy --strict)

Demonstrates:

- Fully annotating all class methods with proper type hints (e.g., `name: str`, `other: object`, `-> bool`).
- Successfully running the `mypy --strict` command on the codebase without triggering any errors or warnings.

Shows that:

- Python can enforce strict type safety using external linters, catching potential type-related bugs before the code even runs.
- Type annotations act as reliable, built-in documentation, making it instantly clear what kind of data each magic method expects to receive and return (e.g., ensuring `__eq__` always returns a `bool` and safely handles any `object`).