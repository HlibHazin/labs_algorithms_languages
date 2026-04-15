from typing import Protocol
from dataclasses import dataclass
from abc import ABC, abstractmethod

class Serializable(Protocol):
    def serialize(self) -> str:
        ...

def export(obj: Serializable) -> None:
    print(obj.serialize())

class StudentRegular:
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"StudentRegular(Name: {self.name}, Group: {self.group}, Grade: {self.average_grade})"

@dataclass
class StudentData:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentData(Name: {self.name}, Group: {self.group}, Grade: {self.average_grade})"

@dataclass(slots=True)
class StudentSlots:
    name: str
    group: str
    average_grade: float

    def serialize(self) -> str:
        return f"StudentSlots(Name: {self.name}, Group: {self.group}, Grade: {self.average_grade})"

class SerializableABC(ABC):
    @abstractmethod
    def serialize(self) -> str:
        pass

class StudentABC(SerializableABC):
    def __init__(self, name: str, group: str, average_grade: float) -> None:
        self.name = name
        self.group = group
        self.average_grade = average_grade

    def serialize(self) -> str:
        return f"StudentABC(Name: {self.name}, Group: {self.group}, Grade: {self.average_grade})"

# ================================
# ======== OUTPUT RESULTS ========
# ================================

# === Task A: Regular class (duck typing) ===
print("--- Task A ---")
student_a = StudentRegular(name="Glib", group="KN-124", average_grade=95.5)
export(student_a)
print("What do we see?: The regular class serializes successfully.")
print("Why does it work?: Duck typing: it has the required 'serialize()' method.\n")

# === Task B: Dataclass implementation ===
print("--- Task B ---")
student_b = StudentData(name="Mykyta", group="KN-123", average_grade=88.0)
export(student_b)
print("What do we see?: The dataclass works exactly the same.")
print("Why does it work?: @dataclass handles boilerplate; our method satisfies the Protocol.\n")

# === Task C: Slots ===
print("--- Task C ---")
student_c = StudentSlots(name="Ivan", group="KN-1624", average_grade=75.5)
export(student_c)
print("What do we see?: It serializes, but blocks adding new attributes.")
print("Why does it work?: Slots replace __dict__ with a fixed structure, preventing dynamic attributes.")
try:
    student_c.new_attribute = "Not allowed" # type: ignore[attr-defined]
except AttributeError as e:
    print(f"AttributeError: {e}")

# === Task D: ABC version ===
print("\n--- Task D ---")
student_d = StudentABC(name="Maria", group="KN-123", average_grade=92.0)
export(student_d)
print("What do we see?: The ABC-inherited object works seamlessly.")
print("Why does it work?: Explicit implementation of the abstract method also satisfies the Protocol.")