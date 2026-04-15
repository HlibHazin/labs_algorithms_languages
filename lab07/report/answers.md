# Lab 07: Answers

**Question: 1. What is duck typing?**
* **Definition**: Duck typing is a programming concept where the suitability of an object is determined by the presence of certain methods and properties, rather than its actual explicit type or inheritance chain.
* **Purpose**: It allows for flexible, dynamic polymorphism where unrelated classes can be used interchangeably as long as they implement the expected behavior ("If it walks like a duck and quacks like a duck, it must be a duck").
* **Limitation/Failure case**: If a required method is missing or incorrectly named, the type checker might not catch it (without strict typing enabled), and the program will crash unexpectedly with an `AttributeError` at runtime when trying to execute that method.

---

**Question: 2. How does Protocol differ from ABC?**
* **Definition**: `Protocol` implements *structural* subtyping (implicit typing), meaning a class only needs to have the matching methods and attributes. `ABC` implements *nominal* subtyping (explicit typing), requiring a class to formally declare inheritance from the abstract base class.
* **Relationship**: Protocol focuses purely on what an object *does* (its external shape), while ABC defines what an object *is* (its explicit place in the inheritance tree).
* **Limitation/Failure case**: Protocols can accidentally match unrelated classes that just happen to share a method name (e.g., two completely different objects having a `close()` method). ABCs prevent this accidental structural matching by forcing explicit inheritance.

---

**Question: 3. Does Protocol require inheritance? Why or why not?**
* **Mechanism**: No, `Protocol` does not require any inheritance. It relies entirely on structural typing under the hood.
* **Purpose**: Static type checkers (like mypy) inspect the class's shape. If the methods and signatures perfectly match the Protocol's definition, the class is considered a valid subtype automatically, keeping class definitions decoupled.
* **Limitation/Failure case**: Because inheritance isn't explicitly declared, a developer might rename or alter a method in a concrete class during refactoring without realizing it silently breaks the Protocol contract, which can only be caught by a type checker or during specific function calls.

---

**Question: 4. What problem does ABC solve?**
* **Mechanism**: ABC solves the problem of enforcing a strict, explicit contract for subclasses through the `@abstractmethod` decorator.
* **Purpose**: It guarantees that any concrete subclass completely implements specific, critical methods *before* an object can even be created, establishing a strong, predictable hierarchy.
* **Limitation/Failure case**: ABC strictly prevents object creation if even a single abstract method is left unimplemented. Attempting to instantiate an incomplete subclass will immediately raise a `TypeError`. It also forces rigid inheritance, which can lead to complex, tightly coupled code structures.

---

**Question: 5. What does @dataclass generate automatically?**
* **Mechanism**: The `@dataclass` decorator automatically generates boilerplate "dunder" (magic) methods based entirely on the type-annotated fields provided in the class.
* **Purpose**: It instantly creates methods like `__init__()`, `__repr__()`, and `__eq__()` behind the scenes, saving developers from writing repetitive setup code for data-centric objects.
* **Limitation/Failure case**: Dataclasses do not enforce data types at runtime by default. If a field is annotated as `age: int` but instantiated with `age="twenty"`, the dataclass will silently accept the string, which can cause severe `TypeError` failures later when math operations are attempted on that attribute.

---

**Question: 6. What changes when using slots?**
* **Mechanism**: Using `@dataclass(slots=True)` tells Python to allocate a fixed, predetermined amount of memory for specific attributes, completely removing the dynamic `__dict__` storage from the object.
* **Purpose**: This heavily reduces memory consumption per object and slightly improves the speed of reading/writing attributes, which is highly beneficial when working with massive datasets.
* **Limitation/Failure case**: Slots introduce strict structural rigidity. You are completely blocked from dynamically adding new attributes to an instance after it is created. Attempting to do so (e.g., `obj.new_data = 123`) will immediately crash the program with an `AttributeError`.

---

**Question: 7. Why does Protocol work with different implementations (regular class, dataclass, slots)?**
* **Mechanism**: Protocol evaluates only the external, public "shape" of an object (specifically, whether it exposes the required method signatures like `serialize(self) -> str`), completely ignoring its internal structure.
* **Purpose**: It abstracts away memory management and initialization details. The Protocol doesn't care if the object was built with a manual `__init__`, an automatic `@dataclass`, uses a dynamic `__dict__`, or uses fixed `slots`.
* **Limitation/Failure case**: This extreme flexibility means Protocol cannot enforce how data is managed internally. If a system requires highly optimized memory usage (like slots) to prevent crashing, a Protocol cannot enforce this requirement; an inefficient regular class that structurally matches the Protocol would still be accepted, potentially leading to OutOfMemory (OOM) errors in large-scale applications.