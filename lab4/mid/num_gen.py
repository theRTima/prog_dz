import random

def rand_gen(beg, end, count):
    for i in range(count):
        yield random.randint(beg, end)

for i, num in enumerate(rand_gen(1, 100, 5)):
    print(f"число {i+1}: {num}")