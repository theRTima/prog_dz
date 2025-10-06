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

first_check = True

while True:
    if(first_check == True):
        first_check = False
    else:
        print("введите число")
        first_num = float(input())
    print("выберите действие")
    print("1 - + ")
    print("2 - * ")
    print("3 - - ")
    print("4 - / ")

    choice = int(input())

    if choice == 1:
        print(addition(first_num, second_num))
        second_num = addition(first_num, second_num)
    elif choice == 2:
        print(multiplication(first_num, second_num))
        second_num = multiplication(first_num, second_num)
    elif choice == 3:
        print(subtraction(first_num, second_num))       
        second_num = subtraction(first_num, second_num) 
    elif choice == 4:
        print(division(first_num, second_num))
        second_num = division(first_num, second_num)    
    else:
        print("ошибка ввода") 