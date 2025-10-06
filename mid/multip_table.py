first_num = input()
second_num = input()

answer = int(first_num) * int(second_num)
bin_answer = bin(answer)[2:]
oct_answer = oct(answer)[2:]
hex_answer = hex(answer)[2:]

print(answer)
print(bin_answer)
print(oct_answer)
print(hex_answer)
