import sys

print("//////////////////// Task A: Truthiness ////////////////////")
def task_a_truthiness():
    test_values = [0, 1, [], [1], "", "hello", None]
    
    for val in test_values:
        print(f"value: {repr(val):<1} -> {bool(val)}")

task_a_truthiness()
print()


print("//////////////////// Task B: Identity vs Equality ////////////////////")
def task_b_identity_vs_equality():

    list1 = [1, 2, 3]
    list2 = [1, 2, 3]
    print(f"a == b -> {list1 == list2}") 
    print(f"a is b -> {list1 is list2}") 

    list3 = list1
    print(f"a is c -> {list1 is list3}")

    str1 = "surprise"
    str2 = "surprise"
    print(f"s1 is s2 -> {str1 is str2}")

task_b_identity_vs_equality()
print()


print("//////////////////// Task C: Control Flow ////////////////////")
def describe_number(x):
    if x < 0:
        return "negative" 
    elif x == 0:
        return "zero" 
    elif 0 < x < 10:
        return "small positive" 
    elif x >= 10:
        return "large positive"
    
test_numbers = [-5, 0, 5, 10]
for num in test_numbers:
    print(f"Number {num:2} is {describe_number(num)}")
print()


print("//////////////////// Task D: Pattern Matching ////////////////////")
def task_d_pattern_matching():
    events = [
        ("click", 10, 20),
        ("keypress", "A"),
        ("quit",)
    ]
    
    for event in events:
        match event: 
            case ("click", x, y):
                print(f"click at {x} {y}") 
            case ("keypress", key):
                print(f"key pressed: {key}") 
            case ("quit",):
                print("quit event") 

task_d_pattern_matching()
print()


print("//////////////////// Task E: Comprehensions ////////////////////")
def task_e_comprehensions():

    squares = [x**2 for x in range(1, 21)]
    print(f"Squares 1-20: {squares}")

    even_squares = [x**2 for x in range(1, 21) if (x**2) % 2 == 0]
    print(f"Even squares: {even_squares}")

    square_dict = {x: x**2 for x in range(1, 11)}
    print(f"Dict 1-10: {square_dict}")

task_e_comprehensions()
print()


print("//////////////////// Task F: Generators ////////////////////")
def even_numbers(limit): 
    n = 0
    while n <= limit:
        yield n 
        n += 2

print("Even numbers up to 8:")
for num in even_numbers(8):
    print(num)

result_sum = sum(x**2 for x in range(1000000) if x % 2 == 0)
print(f"\nSum of squares (evens < 1M): {result_sum}")