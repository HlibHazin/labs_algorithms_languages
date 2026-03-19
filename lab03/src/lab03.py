import math

print("//////////////////// Task A: Functions as Objects ////////////////////")
def apply_twice(func, x):
    return func(func(x))

print(f"Result (lambda x+1, 3): {apply_twice(lambda x: x + 1, 3)}") 


print("//////////////////// Task B: Sorting with Lambda  ////////////////////")
def sort_people_example(data):
    by_age = sorted(data, key=lambda p: p[1])
    by_name = sorted(data, key=lambda p: p[0])
    return by_age, by_name

people = [("Alice", 25), ("Bob", 20), ("Carol", 30), ("Dave", 22)] 
age_res, name_res = sort_people_example(people)
print(f"Sorted by age: {age_res}") 
print(f"Sorted by name: {name_res}") 


print("//////////////////// Task C: Function Factory ////////////////////")
def make_multiplier(k):
    return lambda x: x * k

times3 = make_multiplier(3) 
print(f"times3(10): {times3(10)}") 


print("//////////////////// Task D: Closure Counter  ////////////////////")
def counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment

c = counter() 
print(f"Calls: {c()}, {c()}, {c()}") 


print("//////////////////// Task E: Lambda vs def ////////////////////")
def square_with_def(x):
    return x * x

square_with_lambda = lambda x: x * x  

val = 5
print(f"def result: {square_with_def(val)}") 
print(f"Lambda result: {square_with_lambda(val)}")


print("//////////////////// Task F: Functional Composition ////////////////////")
def run_processing_pipeline(data):
    return sum(n**2 for n in data if (lambda x: x % 2 == 0)(n))

numbers = [1, 2, 3, 4, 5, 6, 7, 8] 
print(f"Pipeline result: {run_processing_pipeline(numbers)}") 

