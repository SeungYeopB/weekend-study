""" 까먹지않게 기본 별찍기 연습 """

N = int(input())

# for i in range(1, N + 1):
#     for j in range(N - i):
#         print(" ", end="")
#     for j in range(2 * i - 1):
#         print("*", end="")
#     print()

#     N = int(input())

# for i in range(1, N + 1):
#     print(" " * (N - i), end="")
#     if i == 1:
#         print("*", end="")
#     elif 1 < i and i < N:
#         print("*" + " " * (2 * i - 3) + "*", end="")
#     else:
#         print("*" * (2 * i - 1), end="")
#     print()

# for i in range(1, N + 1):
#     print(" " * (N - i), end="")
#     for j in range(i):
#         print("*", end=" ")
#     print()


# N = int(input())

# for i in range(1, N + 1):
#     for j in range(N - i):
#         print(" ", end="")
#     for j in range(i):
#         print("*", end="")
#     print()


# for i in range(N):
#     for j in range(2 * N):
#         if (i + j) % 2 == 0:
#             print(" ", end="")
#         else:
#             print("*", end="")
#     print()

for i in range(1, N + 1):
    print(" " * (N - i), end="")
    if i == 0:
        print("*", end="")
    elif 1 < i and i < N:
        print("*" + " " * (2 * i - 3) + "*", end="")
    else:
        print("*" * (2 * i - 1), end="")
    print()
for i in range(1, N):
    print(" " * i, end="")
    if i == N - 1:
        print("*", end="")
    else:
        print("*" + " " * ((2 * N - (2 * i + 3))) + "*", end="")
    print()
