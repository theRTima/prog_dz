def map_sqr():
    numbers = list(range(1, 11))
    squares = list(map(lambda x: x**2, numbers))
    return squares

result = map_sqr()
for i,square in enumerate(result):
    print(f"{i+1}^2 = {square}")