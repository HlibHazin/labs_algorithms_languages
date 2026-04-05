# Lab 05: Answers

**Question: What is the purpose of type hints in Python?**
* **Definition**: Type hints are annotations added to variables, function parameters, and return values to indicate their expected data types. 
* **Purpose**: They are used to improve code reliability and clarity by allowing developers and static type checkers to understand the expected data structures before the code runs.

---

**Question: What is the difference between Any and a generic type (T)?**
* **Mechanism**: `Any` essentially disables type checking for a variable, allowing it to be of any type at any time. A generic type using `TypeVar` (like `T`), on the other hand, allows a function to accept different types while strictly enforcing consistency. 
* **Usage**: Generics ensure that relationships between types are maintained (e.g., guaranteeing that a function returning the first element of a `list[T]` returns exactly the type `T`).

---

**Question: What does Callable [[int], int] describe?**
* **Definition**: It describes a function type. Specifically, it represents a function that takes a single integer (`int`) as an argument and returns an integer (`int`).
* **Application**: This annotation is typically used when defining higher-order functions that accept another function as a parameter (like passing a specific operation to be applied) or when returning a function from another function.

---

**Question: Why does mypy --strict require more annotations?**
* **Mechanism**: Running mypy with the `--strict` flag enforces a strict type checking discipline across the entire codebase. 
* **Consequence**: It prohibits implicit types and dynamically typed constructs, meaning you must explicitly annotate all function arguments, return types, and collections to ensure the command completes without errors.