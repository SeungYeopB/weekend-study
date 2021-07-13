# N = int(input())

# for i in range(1, N):
#     for j in range(i - 1):
#         print(" ", end="")
#     # 별 출력
#     if i == 1:
#         print("*" * N, end="")
#     else:
#         print("*" + " " * (N - 2) + "*", end="")

#     # 사이 공백
#     for j in range(2 * (N - i) - 1):
#         print(" ", end="")

#     if i == 1:
#         print("*" * N, end="")
#     else:
#         print("*" + " " * (N - 2) + "*", end="")

#     print()

# print(" " * (N - 1) + "*" + " " * (N - 2) + "*" + " " * (N - 2) + "*")

# #    *   * *   *
# #   *   *   *   *
# #  *   *     *   *
# # *****       *****

# # 공백 출력
# for i in range(1, N):
#     for j in range(N - i - 1):
#         print(" ", end="")
#     # 별출력
#     if i == (N - 1):
#         print("*" * N, end="")
#     else:
#         print("*" + " " * (N - 2) + "*", end="")

#     # 공백출력
#     for j in range(2 * i - 1):
#         print(" ", end="")

#     # 별출력
#     if i == (N - 1):
#         print("*" * N, end="")
#     else:
#         print("*" + " " * (N - 2) + "*", end="")
#     print()

# from itertools import combinations

# a = [int(input()) for i in range(9)]
# p = list(combinations(a, 7))

# for i in p:
#     if sum(i) == 100:
#         print(*sorted(i, sep="\n"))
#         break
# 20
# 7
# 23
# 19
# 10
# 15
# 25
# 8
# 13


from sys import stdin

arr = [int(stdin.readline().strip()) for _ in range(9)]
arr.sort()
total = sum(arr)

for i in range(len(arr)):
    for j in range(i + 1, len(arr)):
        if (total - arr[i] - arr[j]) == 100:
            for k in range(len(arr)):
                if k != i and k != j:
                    print(arr[k])
            exit()
