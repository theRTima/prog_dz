first_num = int(input())
second_num = int(input())

while first_num != 0 and second_num != 0:
    if first_num > second_num:
        first_num = first_num % second_num
    else:
        second_num = second_num % first_num

print(first_num+second_num)