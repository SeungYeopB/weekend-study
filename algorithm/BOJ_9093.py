# N = int(input())

# for i in range(N):
#     str_array = input().split(" ")
#     for text in str_array:
#         print(text[::-1], end=" ")
#     print()


N = int(input())


result = 1
for i in range(N, 0, -1):
    result *= i
print(result)
