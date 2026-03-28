# 🐍 Lab 04: Higher-Order Functions, map/filter, Decorators

## 🎯 Goal
The goal of this lab is to practice using higher-order functions and to understand how functions can be used to transform behavior.

---

## 📂 Project Structure


```
lab04/
├── README.md              
├── requirements.txt       
├── report/                
│   └── answers.md
└── src/                   
    └── lab04.py
```
---

## 💻 Install dependencies

```bash
pip install -r lab04/requirements.txt
```

This project uses only the Python standard library.

---

## 🚀 Run the Program

```bash
python lab04/src/lab04.py
```

---


## 🔍 Program Output Overview

The program prints seven clearly labeled sections (A–G). Each section demonstrates a specific Python concept.

---


### A) Higher-Order Function

Demonstrates:

- Implementation of an apply(func, data) function that processes a list without using the built-in
- Passing a lambda expression (lambda x: x * 2) as an argument to multiply elements by 2.

Shows that:

- Functions can be passed as arguments to other functions to transform behavior.
- Custom higher-order functions can easily replicate built-in functional iteration.

---

### B) map

Demonstrates:

- Using the map() function to square all numbers in a list.
- Using map() to convert integer numbers into strings.

Shows that:

- map provides a functional and concise way to apply a transformation to every item in an iterable simultaneously.
- It can seamlessly accept built-in types (like str) or anonymous functions (like lambda) as the transformation logic.
---

### C) filter

Demonstrates:

- Using the filter() function with a lambda expression to keep only even numbers.
- Applying a second filter to keep only numbers greater than 10.

Shows that:

- filter efficiently extracts elements from a sequence that satisfy a specific Boolean condition.
- It creates a clean pipeline for data reduction without needing explicit for loops.

---

### D) map/filter vs comprehension

Demonstrates:

- Solving a two-step sequence (keeping even numbers and squaring them) using a combined map and filter approach.
- Solving the exact same sequence using a single list comprehension.
  
Shows that:

- Both implementations produce the exact same result, demonstrating that comprehensions and functional tools are interchangeable for these tasks.
- List comprehensions often consolidate filtering and mapping into a more readable, single-line expression.
  
---

### E) Simple Decorator

Demonstrates:

- Implementing a @call_counter decorator that tracks how many times a wrapped function is executed.
- Printing the current call number sequentially before the function executes.

Shows that:

- Decorators can modify or enhance function behavior without altering the original function's source code.
- Functions can maintain state (like a .calls attribute) across multiple executions.

---

### F) Decorator with Arguments

Demonstrates:

- A @prefix(text) decorator factory that takes a string argument (e.g., "INFO").
- Prepending the specified string to the result returned by the original function.

Shows that:

- By nesting an additional layer, decorators can accept configuration arguments to customize how they wrap the target function.
- Decorators are highly flexible tools for formatting or logging return values globally.
  
---

### G) Caching Decorator

Demonstrates:

- Applying a custom @cache decorator to a recursive "staircase counting" function.
- Measuring and comparing execution times using the time module for both cached and non-cached versions.

Shows that:

- Caching effectively stores previously computed results to bypass redundant operations when the same arguments are passed.
- Memoization drastically optimizes performance and execution speed for heavy recursive algorithms.
