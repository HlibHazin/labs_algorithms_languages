# Lab 03: Answers

**Question: What does it mean that functions in Python are first-class objects?**
* **Versatility**: It means functions can be assigned to variables, passed as arguments, and created dynamically.
* **Functional Capabilities**: This property allows functions to capture variables from their environment (closures) and enables basic functional composition.

---

**Question: What is the difference between a function defined with `def` and a lambda expression?**
* **Structure**: A function defined with `def` is a standard named block, whereas a `lambda` expression is an anonymous inline expression.
* **Usage**: Lambda expressions are particularly useful for short operations, like defining keys for the `sorted` function when sorting by age or name.

---

**Question: What is a closure?**
* **Environmental Link**: A closure is a function that captures and stores variables from its surrounding environment, even after the outer function has finished execution.
  
 ---

**Question: In what situations are closures useful?**
* **State Management**: They are useful for creating "function factories" (like a multiplier) or counters that need to maintain an internal state without using classes.

---

