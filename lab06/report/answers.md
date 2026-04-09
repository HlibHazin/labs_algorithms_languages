# Lab 06: Answers

**Question: What is stored in obj.__dict__?**
* **Definition**: It stores a dictionary (or mapping object) that contains all the dynamically created, mutable attributes specific to that exact instance of the class.
* **Purpose**: It allows Python to maintain the state of the object internally, mapping attribute names (as string keys) to their current data values, enabling direct inspection or modification of the object's state.

---

**Question: What is the difference between a class and an object?**
* **Definition**: A class is a blueprint or template that defines the structure (attributes) and behavior (methods) of a potential entity. An object is a concrete instance created from that blueprint.
* **Relationship**: While a class exists as an abstract definition in the code, an object occupies actual memory space and holds its own unique set of real data.

---

**Question: What does __init__ do?**
* **Mechanism**: The `__init__` method (initializer) is automatically called by Python immediately after a new object is created in memory.
* **Purpose**: It is used to set up the initial state of the newly created object by assigning starting values to its specific instance attributes (e.g., `self.name = name`).

---

**Question: Who calls __str__, and when?**
* **Mechanism**: It is automatically called under the hood by built-in Python functions like `str()`, `print()`, `format()`, and when evaluating f-strings.
* **Purpose**: It is invoked whenever the system needs a human-readable, informal string representation of the object, typically for displaying clear information to an end-user.

---

**Question: What is the difference between == and is?**
* **Mechanism**: The `==` operator checks for *value equality* by calling the object's `__eq__` method to see if the internal data of two objects is equivalent. The `is` operator checks for *identity*.
* **Usage**: You use `==` when you want to know if two separate objects hold the same information (like two students with the exact same name and grades), and `is` when you need to confirm if two variables actually point to the exact same physical object in memory.

---

**Question: Why do we use other: object in __eq__ and __lt__?**
* **Mechanism**: Using `other: object` explicitly tells the static type checker (like mypy) that these comparison methods can receive an argument of *any* type, not just another instance of the same class.
* **Consequence**: It forces the developer to write robust code (typically using `isinstance()`) to handle incompatible types gracefully—returning `False` for `__eq__` or raising a `TypeError` for `__lt__`—which is how Python's object model expects rich comparisons to behave safely.