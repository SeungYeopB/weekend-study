N = int(input())

for i in range(N):
    for j in range(i):
        print(" ",end="")
    for j in range(1,2*N-2*i):
        print("*",end="")
    print()