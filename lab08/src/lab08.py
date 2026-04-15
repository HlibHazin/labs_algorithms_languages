from typing import Any, List, Optional, Type, cast
from types import TracebackType

class GradeDescriptor:
    """Descriptor to validate student grades."""
    def __set_name__(self, owner: Type[Any], name: str) -> None:
        self._name = "_" + name

    def __get__(self, obj: Any, objtype: Any = None) -> int:
        if obj is None:
            raise AttributeError("Cannot access descriptor on class")
        return cast(int, getattr(obj, self._name))

    def __set__(self, obj: Any, value: int) -> None:
        if not isinstance(value, int):
            raise TypeError("Grade must be an integer")
        if not (0 <= value <= 100):
            raise ValueError(f"Grade must be between 0 and 100. Got {value}.")
        setattr(obj, self._name, value)

class Student:
    """Student class with descriptor validation for grade."""
    grade = GradeDescriptor()

    def __init__(self, name: str, group: str, grade: int) -> None:
        self.name = name
        self.group = group
        self.grade = grade

    def __str__(self) -> str:
        return f"Student(name='{self.name}', group='{self.group}', grade={self.grade})"

class StudentIterator:
    """Custom iterator for StudentCollection."""
    def __init__(self, students: List[Student]) -> None:
        self._students = students
        self._index = 0

    def __iter__(self) -> 'StudentIterator':
        return self

    def __next__(self) -> Student:
        if self._index < len(self._students):
            student = self._students[self._index]
            self._index += 1
            return student
        raise StopIteration

class StudentCollection:
    """Collection that acts as both an Iterable and a Context Manager."""
    def __init__(self, students: List[Student]) -> None:
        self._students = students

    def __iter__(self) -> StudentIterator:
        return StudentIterator(self._students)

    def __enter__(self) -> 'StudentCollection':
        print("\n--- Context Manager: Entering the context ---")
        return self

    def __exit__(self, exc_type: Optional[Type[BaseException]], exc_value: Optional[BaseException], traceback: Optional[TracebackType]) -> None:
        print("--- Context Manager: Exiting the context ---")
        if exc_type is not None:
            print(f"Exception handled during exit: {exc_value}")

# ================================
# ======== OUTPUT RESULTS ========
# ================================

students_data = [
    Student("Glib", "KN-124", 85),
    Student("Maria", "KN-123", 92),
    Student("Vlad", "KN-124", 78)
]

# === Task A: Iteration ===
print("\n--- Task A: Iteration ---")
collection = StudentCollection(students_data)
for student in collection:
    print(student)

print("\nWhat do we see? Iterating over StudentCollection using a direct for loop.")
print("Why does it work? The StudentCollection class implements __iter__ returning a custom StudentIterator, which implements __next__.")

# === Task B & D: Context Manager & Integration ===
print("\n--- Task B & D: Context Manager & Integration ---")
with StudentCollection(students_data) as ctx_collection:
    for student in ctx_collection:
        print(f"Student grade: {student.grade}")

print("\nWhat do we see? Entering context, directly iterating over the students, and exiting cleanly.")
print("Why does it work? The 'with' statement invokes __enter__ at the start and __exit__ at the end of the block. Direct iteration works inside because the object is iterable.")

# === Task C: Descriptor ===
print("\n--- Task C: Descriptor ---")
try:
    invalid_student = Student("Test", "GROUP", 120)
except ValueError as e:
    print(f"Validation caught: {e}")

print("\nWhat do we see? Attempting to assign an invalid grade (120) to a student.")
print("Why does it work? The GradeDescriptor intercepts the assignment in __set__ and raises a ValueError before the object state is modified.")