num = int(input())

def recursive_sum(num):
    numbers_array = list(str(num))
    sum = 0

    for i in numbers_array:
        sum += int(i)
    
    if int(sum) < 10:
        return sum
    else:
        return recursive_sum(sum)

print(recursive_sum(num))