import time

#================== TASK A ==================
print("--- Task A: Higher-Order Function ---")

def apply(func, data):
    result = []
    for item in data:
        result.append(func(item))
    return result

res_a = apply(lambda x: x * 2, [1, 2, 3])
print(f"apply(x * 2, [1, 2, 3]): {res_a}")

#================== TASK B ==================
print("\n--- Task B: map ---")

nums_b = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums_b))
stringified = list(map(str, nums_b))

print(f"Original: {nums_b}")
print(f"Squared: {squared}")
print(f"Stringified: {stringified}")

#================== TASK C ==================
print("\n--- Task C: filter ---")

nums_c = [5, 10, 15, 20]
evens = list(filter(lambda x: x % 2 == 0, nums_c))
greater_than_10 = list(filter(lambda x: x > 10, nums_c))

print(f"Original: {nums_c}")
print(f"Evens: {evens}")
print(f"Greater than 10: {greater_than_10}")

#================== TASK D ==================
print("\n--- Task D: map/filter vs comprehension ---")

nums_d = [1, 2, 3, 4, 5, 6, 7, 8]
map_filter_result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums_d)))
comprehension_result = [x**2 for x in nums_d if x % 2 == 0]

print(f"map+filter: {map_filter_result}")
print(f"comprehension: {comprehension_result}")
print(f"Results are equal: {map_filter_result == comprehension_result}")

#================== TASK E ==================
print("\n--- Task E: Simple Decorator ---")

def call_counter(func):
    def wrapper(*args, **kwargs):
        wrapper.calls += 1
        print(f"  [CALL #{wrapper.calls}]")
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@call_counter
def say_hello():
    print("  Hello!")

say_hello()
say_hello()
say_hello()
print(f"Total function calls: {say_hello.calls}")

#================== TASK F ==================
print("\n--- Task F: Decorator with Arguments ---")

def prefix(text):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return f"{text}: {result}"
        return wrapper
    return decorator

@prefix("INFO")
def get_data():
    return "data"

print(get_data())

#================== TASK G ==================
print("\n--- Task G: Caching Decorator ---")

def cache(func):
    memo = {}
    def wrapper(*args):
        if args in memo:
            return memo[args]
        result = func(*args)
        memo[args] = result
        return result
    return wrapper

def staircase_no_cache(n):
    if n < 0: return 0
    if n == 0: return 1
    return staircase_no_cache(n-1) + staircase_no_cache(n-2) + staircase_no_cache(n-3)

@cache
def staircase_cache(n):
    if n < 0: return 0
    if n == 0: return 1
    return staircase_cache(n-1) + staircase_cache(n-2) + staircase_cache(n-3)

n_value = 25

start_time = time.time()
res1 = staircase_no_cache(n_value)
time_no_cache = time.time() - start_time
print(f"Без кешування: результат={res1}, час={time_no_cache:.5f} сек")

start_time = time.time()
res2 = staircase_cache(n_value)
time_cache = time.time() - start_time
print(f"З кешуванням:  результат={res2}, час={time_cache:.5f} сек")
