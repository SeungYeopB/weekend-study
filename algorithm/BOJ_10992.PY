# N = int(input())

# for i in range(1, (N+1)):
#     if i == 1:				# 첫 번째 줄
#         print(' ' * (N - i) + "*")

#     elif i == N:			# 마지막 줄
#         print("*" * (i * 2 - 1))

#     else:				# 중간
#         print(' ' * (N - i) + "*" + ' ' * (i * 2 - 3) + "*")


# N = int(input())

# for i in range(1, N + 1):
#     for j in range(N - i):
#         print(" ", end="")

#     if (i > 1) & (i < N):
#         print("*", end="")
#         for j in range(2 * i - 3):
#             print(" ", end="")
#         print("*")

#     else:
#         for j in range(2 * i - 1):
#             print("*", end="")
#         print()


N = int(input())

for i in range(1, N + 1):
    for j in range(i):
        print("*", end="")
    print()
