# Lab 01: Answers

## Task A: Binding / Rebinding
**Question:** Explain why `b` still refers to the old value after `a = 7`.

**Answer:**
* In Python, names are **bindings** to objects, not variables in the traditional sense.
* The operation `a = 7` is a **rebinding** that changes the name-object relationship for `a`, pointing it to a new object.
* The objects themselves are not modified. Since `b` remains bound to the original object (5), it continues to refer to that value.

---

## Task B: Mutation vs Rebinding
**Question:** Explain why both names see the change and the difference between mutation and rebinding.

**Answer:**
* **Why both names see the change:** After `b = a`, both names are bound to the same list object. Mutating the object through `b` (e.g., via `.append()`) modifies the shared object.
* **Difference:**
    * **Mutation** changes the internal state of an existing object while its identity (id) remains the same.
    * **Rebinding** changes the name-object relationship so the name points to a different object.

---

## Task C: Function Arguments
**Question:** Explain why mutation inside the function affects the caller, while rebinding does not.

**Answer:**
* Function **parameters are new local names**.
* **Argument passing is binding**, not copying; the local name initially points to the same object as the argument.
* **Mutation** inside the function affects the caller because it modifies the shared object.
* **Rebinding** inside the function only changes what the local name points to and does not affect the caller's binding.

---

## Task D: Default Argument Trap
**Question:** Explain why the list keeps growing.

**Answer:**
* In Python, **default values are evaluated only once** when the function is defined.
* The **same object is reused across all calls** to the function.
* Since a list is mutable, every call that modifies it affects this single persistent object.

---

## Task E: Copy Semantics
**Question:** Explain the difference between shallow copy and deep copy.

**Answer:**
* **Shallow copy:** Creates a new container but fills it with references to the original **nested objects**.
* **Deep copy:** Recursively creates copies of both the container and all **nested objects** within it, ensuring complete independence.

---

## Task F: Reference Counting / GC
**Question:** Explain why the result for 5 may look unusual.

**Answer:**
* The high reference count for `5` is due to a **CPython optimization**.
* Small integers are treated as **immortal objects** (pre-allocated and shared globally) to save memory.
* This behavior is an **implementation detail** of CPython and is not guaranteed by the general Python language specification.