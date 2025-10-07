num = input()

def recursive_sum(num):
    numbers_array = list(str(num))
    sum = 0

    for i in numbers_array:
        sum += numbers_array[i]
    
    if len(str(sum)) <= 1:
        return sum
    else:
        return recursive_sum(sum)

recursive_sum(num)