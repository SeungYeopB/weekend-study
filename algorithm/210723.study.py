""" 기본적인 별찍기 알고리즘 매일 반복 연습 """

N = int(input())

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

#     *
#    * *
#   *   *
#  *     *
# *********
#  *     *
#   *   *
#    * *
#     *
