# Lab 02: Answers

## Task A: Truthiness
**Question: Why does Python treat empty containers as False?**
* **Consistency**: Python evaluates any object with a length of 0 (like `[]` or `""`) as `False` to maintain a consistent logic across all collection types.
* **Readability**: It allows for cleaner, "Pythonic" code, enabling developers to use `if container:` instead of more verbose length checks.

---

## Task B: Identity vs Equality
**Question: When should `is` be used instead of `==`?**
* **Singletons**: Use `is` primarily when comparing a variable to unique singletons, most commonly `None` (e.g., `if x is None:`).
* **Identity Check**: Use `is` only when you need to confirm that two variables point to the exact same object in memory, whereas `==` checks if their values are equal.

---

## Task D: Pattern Matching
**Question: Why is `match` convenient for analysing structured data?**
* **Destructuring**: The `match` statement can unpack sequences (like tuples) and bind their elements to variables in a single operation.
* **Readability**: It provides a more declarative and organized way to handle multiple data shapes compared to nested `if-elif` blocks.

---

## Task F: Generators
**1. What is the difference between a list comprehension and a generator expression?**
* **Memory Management**: A list comprehension `[]` builds the entire list in memory at once, while a generator expression `()` produces items one by one on demand.

**2. Why are generators considered lazy?**
* **Deferred Evaluation**: They use "lazy evaluation," meaning they do not compute their next value until it is explicitly requested (e.g., in a loop), which saves system resources.

**3. What happens when a generator finishes execution?**
* **StopIteration**: When a generator has no more values to `yield`, it raises a `StopIteration` exception, which signals to Python's iteration tools to stop the process.
