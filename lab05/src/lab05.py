from typing import List, Optional, Callable, TypeVar

#======== Task A: Basic Type Hints ========
def add(a: int, b: int) -> int:
    return a + b

def square_list(data: List[int]) -> List[int]:
    return [x * x for x in data]

print("Task A:")
print(f"add(5, 7) = {add(5, 7)}")
print(f"square_list([1, 2, 3]) = {square_list([1, 2, 3])}\n")


#======== Task B: Typed Collections ========
def filter_even(data: List[int]) -> List[int]:
    return [x for x in data if x % 2 == 0]

print("Task B:")
print(f"filter_even([1, 2, 3, 4, 5, 6]) = {filter_even([1, 2, 3, 4, 5, 6])}\n")


#======== Task C: Optional ========
def find(data: List[int], x: int) -> Optional[int]:
    if x in data:
        return x
    return None

print("Task C:")
print(f"find([10, 20, 30], 20) = {find([10, 20, 30], 20)}") 
print(f"find([10, 20, 30], 99) = {find([10, 20, 30], 99)}\n")


#======== Task D: Function Type ========
def apply(func: Callable[[int], int], x: int) -> int:
    return func(x)

def double(n: int) -> int:
    return n * 2

def subtract_one(n: int) -> int:
    return n - 1
    
print("Task D:")
print(f"apply(double, 5) = {apply(double, 5)}")
print(f"apply(subtract_one, 5) = {apply(subtract_one, 5)}\n")


#======== Task E: Generics ========
T = TypeVar('T')

def first(items: List[T]) -> T:
    return items[0]

print("Task E:")
print(f"first([100, 200, 300]) = {first([100, 200, 300])}") 
print(f"first(['apple', 'coconut']) = {first(['apple', 'coconut'])}\n")


#======== Task F: Function Returning Function ========
def make_multiplier(k: int) -> Callable[[int], int]:
    def multiplier(x: int) -> int:
        return x * k
    return multiplier

print("Task F:")
times_five = make_multiplier(5)
print(f"times_five(10) = {times_five(10)}\n")


#======== Task G: Pipeline ========
print("Task G:")
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
pipeline_result: int = sum((x ** 2 for x in filter(lambda n: n % 2 == 0, numbers)))
print(f"Pipeline result for {numbers} = {pipeline_result}\n")