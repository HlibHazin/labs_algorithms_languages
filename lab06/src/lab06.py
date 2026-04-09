class Student:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        """Initialize student attributes."""
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def __str__(self) -> str:
        """Human-readable object description."""
        return f"Student: {self.name} (group {self.group}, average grade = {self.average_grade})"

    def __repr__(self) -> str:
        """Official (formal) string representation for developers."""
        return f"Student(name={self.name!r}, group={self.group!r}, average_grade={self.average_grade!r})"

    def __eq__(self, other: object) -> bool:
        """Check for equality between two students."""
        if not isinstance(other, Student):
            return False
        return (self.name == other.name and
                self.group == other.group and
                self.average_grade == other.average_grade)

    def __lt__(self, other: object) -> bool:
        """Define sorting order by average grade."""
        if not isinstance(other, Student):
            raise TypeError(f"Comparison between 'Student' and '{type(other).__name__}' is not supported")
        return self.average_grade < other.average_grade

# ================================
# ======== OUTPUT RESULTS ========
# ================================

# === Task A: Initialization ===
print("--- Task A ---")
student1 = Student("Glib", "KN-124", 95.5)
print(f"Name: {student1.name}")
print(f"Group: {student1.group}")
print(f"Average Grade: {student1.average_grade}\n")

# === Task B: __dict__ Structure ===
print("--- Task B ---")
print(f"Original __dict__: {student1.__dict__}")
student1.__dict__["average_grade"] = 98.0
print(f"Updated __dict__: {student1.__dict__}")
print(f"New average_grade value: {student1.average_grade}\n")

# === Task C & Task D: str and repr ===
print("--- Task C & D ---")
print(f"str(): {str(student1)}")
print(f"repr(): {repr(student1)}\n")

# === Task E: Equality (__eq__) ===
print("--- Task E ---")
student2 = Student("Olena", "KN-1625", 91.0)
student3 = Student("Glib", "KN-124", 98.0)
print(f"student1 == student2 (different): {student1 == student2}")
print(f"student1 == student3 (same): {student1 == student3}")
print(f"student1 == 'some string': {student1 == 'some string'}\n")

# === Task F & Task G: Sorting (__lt__) ===
print("--- Task F & G ---")
students = [
    Student("Ivan", "KN-125", 88.5),
    student1,  
    student2, 
    Student("Maria", "KN-123", 99.9)
]

students.sort()

for s in students:
    print(s)