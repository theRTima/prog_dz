def addition(first_num, secong_num):
    return (first_num + secong_num)

def multiplication(first_num, secong_num):
    return (first_num * secong_num)

def subtraction(first_num, secong_num):
    return (first_num - secong_num)

def division(first_num, secong_num):
    return (first_num / secong_num)

print("введите два числа, выберите действие")
first_num = float(input())
second_num = float(input())

print("1 - + ")
print("2 - * ")
print("3 - - ")
print("4 - / ")

choice = int(input())

