from functools import reduce

def pipeline():
    data = list(range(1, 21))
    print(f"данные: {data}")

    result = reduce(lambda x, y: x + y, 
                    filter(lambda x: x > 100,
                           map(lambda x: x**2,filter(lambda x: x % 2 == 0, data))
                    )
    )
    
    print(f"результат {result}")
    
pipeline()