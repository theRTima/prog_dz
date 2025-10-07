first_num = input("первое число ")
second_num = input("второе число ")
base = int(input("основание системы "))

first_num = int(first_num,base)
second_num = int(second_num,base)

def converter(
        num, base):
    
    all_base = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    negative_check = False

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

answer = first_num*second_num
first_num = int(converter(first_num,base))
second_num = int(converter(second_num,base))
answer = converter(answer,base)

print(f"число {first_num} в системе с основанием", base, ":", first_num)
print(f"число {second_num} в системе с основанием", base, ":", second_num)
print(f"{first_num} * {second_num} в системе с основанием", base, ":", answer)