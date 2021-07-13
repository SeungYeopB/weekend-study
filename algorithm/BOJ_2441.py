N = int(input())

for i in range(N):
    print(" " * i, "*" * (N - i), end="")
    print()

N = int(input())

for i in range(N):
    for j in range(i):
        print(" ", end="")
    for j in range(N - i):
        print("*", end="")
    print()
