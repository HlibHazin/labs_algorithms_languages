# 🐍 Lab 05: Type Hints, Generics, Mypy

## 🎯 Goal
The goal of this lab is to practice using type hints and to understand how static typing improves code reliability and clarity.

---

## 📂 Project Structure


```
lab05/
├── README.md              
├── requirements.txt       
├── report/                
│   └── answers.md
└── src/                   
    └── lab05.py
```
---

## 💻 Install dependencies

```bash
pip install -r lab05/requirements.txt
```
---

## 🚀 Run the Program

```bash
python lab05/src/lab05.py
```

---


## 🔍 Program Output Overview

The program prints seven clearly labeled sections (A–G). Each section demonstrates a specific Python typing concept.

---

### A) Basic Type Hints

Demonstrates:

- Adding standard type annotations (`int`, `List[int]`) to basic functions like `add(a, b)` and `square_list(data)`.
- Executing these functions to prove they work normally at runtime.

Shows that:

- Type hints define the expected input parameters and return types without altering runtime behavior.
- They make the code self-documenting and allow static checkers (like mypy) to catch errors before execution.

---

### B) Typed Collections

Demonstrates:

- Implementing a `filter_even(data: List[int]) -> List[int]` function.
- Processing a typed list and returning a new typed list containing only even numbers.

Shows that:

- Type hints can specify not just the collection type (like `list`), but also the type of elements inside it.
- This ensures data consistency when performing list operations.

---

### C) Optional

Demonstrates:

- Implementing a `find(data, x)` function that returns the value if found, or `None` if it is missing.
- Using `Optional[int]` (or `int | None`) as the return type annotation.

Shows that:

- `Optional` explicitly warns developers and type checkers that a function might not return a concrete value.
- It forces the caller to handle potential `None` edge cases safely.

---

### D) Function Type

Demonstrates:

- Implementing an `apply(func: Callable[[int], int], x: int)` higher-order function.
- Passing different functions (like `double` and `subtract_one`) as arguments to be executed.

Shows that:

- The `Callable` type hint effectively describes functions passed as arguments.
- It enforces strict rules on what kind of parameters the passed function must accept and what it must return.

---

### E) Generics

Demonstrates:

- Creating a `first(items: List[T]) -> T` function using a generic `TypeVar('T')`.
- Calling the function with different data types (e.g., a list of integers and a list of strings).

Shows that:

- Generics allow functions to remain flexible and operate on multiple data types.
- Unlike `Any`, generics strictly enforce the relationship between inputs and outputs (e.g., returning the exact type `T` that was inside the list).

---

### F) Function Returning Function

Demonstrates:

- Implementing a `make_multiplier(k: int)` factory function.
- Returning an inner closure function annotated as `Callable[[int], int]`.

Shows that:

- Type hints can accurately describe complex functional concepts, such as closures.
- It clarifies the signature of the dynamically generated function that is being returned.

---

### G) Pipeline

Demonstrates:

- Combining functional tools (lambdas, `filter`, generator expressions, and `sum`) into a single processing pipeline.
- Explicitly annotating the initial data list and the final result variable.

Shows that:

- Functional programming paradigms can seamlessly coexist with strict static typing.
- Complex, chained transformations can be type-checked efficiently to produce safe and predictable results.