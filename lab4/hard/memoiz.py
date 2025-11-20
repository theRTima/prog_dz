import random

def memoize(func):
    cache = {}
    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper

@memoize
def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n-1)

print("\nфакториалы ")
for i in range(1, 6):
    print(f"{i}! = {factorial(i)}") 