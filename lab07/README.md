# 🐍 Lab 07: Behavior, Protocols, ABC, Dataclasses, Slots

## 🎯 Goal
The goal is to understand how Python defines “type” through behavior rather than inheritance.

## 📂 Project Structure


```
lab07/
├── README.md              
├── requirements.txt       
├── report/                
│   └── answers.md
└── src/                   
    └── lab07.py
```
---

## 💻 Install dependencies

```bash
pip install -r lab07/requirements.txt
```
---

## 🚀 Run the Program

```bash
python lab07/src/lab07.py
```

---

---

## 🚀 Run mypy --strict

```bash
mypy --strict lab07/src/lab07.py
```

---

## 🔍 Program Output Overview

The program prints four clearly labeled sections (A–D), plus a static type checking verification. Each section demonstrates a specific concept of the Python Object Model related to structural and nominal typing.

---

### A) Regular Class (Duck Typing)

Demonstrates:

- Instantiating a standard `StudentRegular` class that manually implements a `serialize()` method.
- Passing this object to an `export()` function that explicitly expects a `Serializable` Protocol.

Shows that:

- Python natively supports structural subtyping (duck typing).
- An object does not need to explicitly inherit from a base class or interface; as long as it has the required methods (the right "shape"), it perfectly satisfies the Protocol contract.

---

### B) Dataclass Implementation

Demonstrates:

- Using the `@dataclass` decorator to generate a `StudentData` class with the same fields.
- Implementing the `serialize()` method and verifying it interacts with the `export()` function identically to the regular class.

Shows that:

- Dataclasses significantly reduce boilerplate code by automatically generating essential "dunder" methods (like `__init__`).
- Custom methods integrate seamlessly into dataclasses, allowing them to cleanly fulfill Protocol requirements.

---

### C) Slots (`slots=True`)

Demonstrates:

- Creating a `StudentSlots` dataclass with `slots=True` to alter its internal memory management.
- Intentionally attempting to assign a new, dynamic attribute (`new_attribute`) to the instance at runtime, which successfully triggers an `AttributeError`.

Shows that:

- Using slots replaces the dynamic `__dict__` storage mechanism with a fixed, memory-optimized structure.
- This strictly restricts the object's structure, preventing the creation of unpredicted dynamic attributes, while maintaining full compatibility with the structural Protocol.

---

### D) Abstract Base Class (ABC)

Demonstrates:

- Defining an explicit interface using `SerializableABC` and `@abstractmethod`.
- Creating a concrete `StudentABC` class that explicitly inherits from the ABC and implements the required `serialize()` method.

Shows that:

- ABCs implement nominal subtyping, enforcing a strict, explicit contract that prevents an object from being instantiated if required methods are missing.
- A single concrete class can seamlessly satisfy both explicit inheritance (ABC) and implicit structural typing (Protocol) simultaneously.

---
