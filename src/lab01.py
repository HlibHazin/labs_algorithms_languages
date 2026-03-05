import sys
import copy

print()

print("//////////////// TASK A — Binding vs Rebinding : ////////////////")

print("\nInitial:")
a = 5
b = a 
print("a = ", a, ", b = ", b, sep="")
print("id(a) =", id(a))
print("id(b) =", id(b))

print("\nAfter rebinding a = 7:")
a = 7
print("a = ", a, ", b = ", b, sep="")
print("id(a) =", id(a))
print("id(b) =", id(b))


print("\n\n//////////////// TASK B — Mutation vs Rebinding : ////////////////")

a = [1, 2]
b = a

print("\nInitial:")
print("a =", a)
print("b =", b)

print("\nAfter mutation:")
b.append(3)
print("a =", a)
print("b =", b)

print("\nid(a) == id(b) is", id(a) == id(b))


print("\n\n//////////////// TASK C — Function arguments are new bindings : ////////////////")

def mutate_list(lst):
    lst.append(1)

def rebind_list(lst):
    lst = [5, 10]

a = []

print("\nBefore call:")
print("a =", a)

print("\nAfter mutate_list(a):")
mutate_list(a)
print("a =", a)

print("\nAfter rebind_list(a):")
rebind_list(a)
print("a =", a)


print("\n\n//////////////// TASK D — Default argument trap : ////////////////")

def f(x=[]):
    x.append(1)
    return x

print("\nFirst call:")
print(f())

print("\nSecond call:")
print(f())


print("\n\n//////////////// TASK E — Copy semantics (shallow vs deep) : ////////////////")

a = [[1, 2]]
b = a.copy()
c = copy.deepcopy(a)

print("\nOriginal:")
print("a =", a)

b[0].append(3)

print("\nAfter modifying b:")
print("a =", a)
print("b =", b)
print("c =", c)


print("\n\n//////////////// TASK F — Reference counting / GC (CPython) : ////////////////")

def refcount(obj):
    return sys.getrefcount(obj)

x = []
print("\nInitial refcount:")
print(refcount(x))

y = x
print("\nRefcount after y = x:")
print(refcount(x))

print("\nRefcounts for integers:")
print("\nRefcount(5) =", sys.getrefcount(5))       
print("Refcount(123456) =", sys.getrefcount(123456))

print()