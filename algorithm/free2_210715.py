# 둘레 : 2 * 원주율 * 반지름
# 넓이 : 원주율 * 반지름 * 반지름

# str_input = input("원의 반지름 입력>")
# num_input = int(str_input)
# print()
# print("반지름:", num_input)
# print("둘레:", 2 * 3.14 * num_input)
# print("넓이:", 3.14 * num_input ** 2)


# a = input("문자열 입력> ")
# b = input("문자열 입력 >")

# print(a, b)
# c = a
# a = b
# b = c
# print(a, b)


# output_a = "{:+5d}".format(52)
# print(output_a)

hour, minute = map(int, input().split())

if minute > 44:
    print(hour, minute - 45)
elif minute <= 44 and hour >= 1:
    print(hour - 1, minute + 15)
else:
    print(23, minute + 15)
