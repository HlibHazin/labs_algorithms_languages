# Lab 04: Answers

**Question: What is a higher-order function?**
* **Definition**: A higher-order function is a function that takes other functions as arguments or returns a function as its result.
* **Purpose**: They are used to transform behavior and allow functions to be treated as data.

---

**Question: What is the difference between map and list comprehension?**
* **Mechanism**: `map` is a functional transformation that applies a function to an iterable, whereas a list comprehension is a syntax for creating a new list from an existing iterable.
* **Usage**: Both can achieve similar results, but comprehensions can often combine mapping and filtering (like keeping even numbers and squaring them) into a single, concise expression.

---

**Question: What is a decorator?**
* **Concept**: A decorator is a higher-order function used to modify or transform the behavior of another function.
* **Implementation**: It wraps an original function to execute additional code, such as counting the number of function calls, without altering the original function's source code.

---

**Question: What is the difference between a simple decorator and a decorator with arguments?**
* **Structure**: A simple decorator takes only the target function as its parameter, while a decorator with arguments requires an outer factory function to accept custom parameters (like a string prefix) before returning the actual decorator.
* **Flexibility**: Decorators with arguments provide more dynamic control, allowing you to customize the wrapper's behavior at the point where it is applied.

---

**Question: Why is caching useful?**
* **Performance**: Caching stores previously computed results and returns those cached results when the exact same arguments are used again.
* **Optimization**: This avoids repeated computations, which drastically reduces execution time for heavy recursive algorithms like staircase counting.