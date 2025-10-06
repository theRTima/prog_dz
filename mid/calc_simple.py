def addition(first_num, secong_num):
    return float(first_num + secong_num)

def multiplication(first_num, secong_num):
    return float(first_num * secong_num)

def subtraction(first_num, secong_num):
    return float(first_num - secong_num)

def division(first_num, secong_num):
    return float(first_num / secong_num)

print("введите два числа, выберите действие")
first_num = float(input())
second_num = float(input())

first_check = True

while True:
    if(first_check == True):
        first_check = False
    else:
        print("введите число")
        second_num = float(input())

    print("действия")
    print("+")
    print("*")
    print("-")
    print("/")

    choice = input()

    if choice == "+":
        print(addition(first_num, second_num))
        first_num = addition(first_num, second_num)
    elif choice == "*":
        print(multiplication(first_num, second_num))
        first_num = multiplication(first_num, second_num)
    elif choice == "-":
        print(subtraction(first_num, second_num))       
        first_num = subtraction(first_num, second_num) 
    elif choice == "/" and second_num != 0:
        print(division(first_num, second_num))
        first_num = division(first_num, second_num)    
    else:
        print("ошибка ввода")
        exit()