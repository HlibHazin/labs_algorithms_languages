# Lab 08: Answers

**Question: 1. How does a for loop work with custom objects?**
* **Mechanism**: The `for` loop first calls the `__iter__()` magic method on the object to retrieve an iterator. Then, it repeatedly calls the `__next__()` method on that iterator to fetch items one by one.
* **Purpose**: It provides a native, highly readable way to traverse elements inside custom data structures without requiring manual index tracking.
* **Limitation/Failure case**: **If `StopIteration` is not raised** when the underlying data is exhausted, the `for` loop will never know it needs to stop. This turns the loop into an infinite loop, which will eventually freeze the application or crash the system due to resource exhaustion.

---

**Question: 2. What methods are required for iteration?**
* **Definition**: To fulfill the Iterator Protocol, an object must implement two specific magic methods: `__iter__()` and `__next__()`.
* **Purpose**: `__iter__()` guarantees that the object returns itself (or another valid iterator), and `__next__()` guarantees there is a standardized mechanism to fetch the next sequential value. 
* **Limitation/Failure case**: If a class implements `__iter__` but fails to implement `__next__`, Python will raise a `TypeError` when a loop is initiated, explicitly stating that the returned object is not a valid iterator.

---

**Question: 3. How does the with statement work internally?**
* **Mechanism**: When execution enters a `with` block, Python invokes the object's `__enter__()` method. When execution leaves the block, Python unconditionally invokes the `__exit__()` method.
* **Purpose**: It ensures reliable, automatic resource management (like closing files, releasing locks, or cleaning up data), guaranteeing that setup and teardown occur as a matched pair.
* **Limitation/Failure case**: **If `__exit__` is missing** from the class definition, the object violates the Context Manager protocol. Attempting to use this object in a `with` statement will immediately crash the program with an `AttributeError` upon entering the block, as Python cannot guarantee safe teardown.

---

**Question: 4. When is exit called?**
* **Mechanism**: The `__exit__()` method is called at the exact moment the execution flow leaves the indented `with` block.
* **Purpose**: To guarantee that cleanup code runs reliably under all circumstances—whether the block finished normally, executed a `return` statement, or was interrupted by an error.
* **Limitation/Failure case**: If an exception occurs inside the block and `__exit__` does not explicitly return `True` to suppress it, the exception will propagate outward. If left unhandled by an external `try/except` block, it will abruptly terminate the program.

---

**Question: 5. What problem do descriptors solve?**
* **Mechanism**: Descriptors intercept standard attribute access (getting, setting, deleting) using the `__get__()`, `__set__()`, and `__delete__()` methods at the class level.
* **Purpose**: They solve the problem of code duplication by allowing developers to encapsulate complex logic—such as type checking, bounds checking, or logging—into a single, reusable class instead of writing repetitive getter/setter properties for every attribute.
* **Limitation/Failure case**: **If validation is not implemented** inside the descriptor's `__set__` method (or if the descriptor is bypassed altogether), invalid data can be assigned to the object's attributes (e.g., giving a student a grade of 120 or -5). This corrupts the object's internal state and will likely cause silent, critical failures in downstream business logic or calculations.

---

**Question: 6. What happens if a descriptor is not used?**
* **Mechanism**: Without a descriptor, attributes are written directly into the instance's dynamic `__dict__` storage.
* **Purpose**: This default behavior is fast and memory-efficient for simple data objects that don't require strict rules or side effects upon modification.
* **Limitation/Failure case**: As mentioned above, bypassing descriptors means relying entirely on the developer to manually check values before assignment. If they forget, bad data bypasses the system's intended constraints, leading to data integrity issues.

---

**Question: 7. Why is direct iteration preferred over index-based loops in Python?**
* **Mechanism**: Direct iteration (`for item in collection`) asks the object for its next element via the Iterator Protocol. Index-based loops (`for i in range(len(collection))`) calculate a length and perform repetitive positional lookups (`collection[i]`).
* **Purpose**: Direct iteration is idiomatic ("Pythonic"), cleaner to read, and works universally across all iterable types—even those that do not support indexing natively (like sets, data streams, or generators).
* **Limitation/Failure case**: Index-based loops are inherently fragile and prone to "Index Out of Bounds" (`IndexError`) exceptions if the collection dynamically changes size during the loop, or if the developer makes an "off-by-one" calculation error. Direct iteration entirely prevents these positional errors.