first_num = int(input())
second_num = int(input())

def gcd(
        first_num, second_num):
    while first_num != 0 and second_num != 0:
        if first_num > second_num:
            first_num = first_num % second_num
        else:
            second_num = second_num % first_num
    return first_num + second_num

print(gcd(first_num,second_num))