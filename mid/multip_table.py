first_num = int(input("первое число "))
second_num = int(input("второе число "))
base = int(input("основание системы "))

def converter(num, base):
    all_base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if base > 36:
        print("основание системы больше 36")
        exit()
    if num == 0:
        return "0"
    if num < 0:
        negative_check = True
    
    num = abs(num)

    result = ""
    while num > 0:
        result = all_base[num%base]+result
        num = num // base
    
    if negative_check == True:
        return "-"+result
    else:
        return result

if base == 2:
    first_num = bin(first_num)[2:]
    second_num = bin(second_num)[2:] 
    answer = bin(answer)[2:]
elif base == 8:
    first_num = oct(first_num)[2:]
    second_num = oct(second_num)[2:]
    answer = oct(answer)[2:]
elif base == 16:
    first_num = hex(first_num)[2:]
    second_num = hex(second_num)[2:]
    answer = hex(answer)[2:]
elif base == 10:
    print("число 1 в системе с основанием", base, ":", first_num)
    print("число 2 в системе с основанием", base, ":", second_num)
    print("произведение в системе с основанием", base, ":", answer)
    exit()

first_num = converter(first_num,base)
second_num = converter(second_num,base)
answer = first_num*second_num

print("число 1 в системе с основанием", base, ":", first_num)
print("число 2 в системе с основанием", base, ":", second_num)
print("произведение в системе с основанием", base, ":", answer)