from functools import reduce

def pipeline_processing():
    data = list(range(1, 21))
    print(f"исходные данные: {data}")
    
    # Pipeline:
    # 1. Фильтрация четных чисел
    # 2. Возведение в квадрат
    # 3. Фильтрация чисел > 100
    # 4. Суммирование
    result = reduce(
        lambda x, y: x + y,
        filter(
            lambda x: x > 100,
            map(
                lambda x: x**2,
                filter(lambda x: x % 2 == 0, data)
            )
        )
    )
    
    print(f"Результат pipeline: {result}")
    
pipeline_processing()