N = int(input())

for i in range(2*N):
    for j in range(N):
        if (i+j)%2 == 0:
            print("*",end="")
        else:
            print(" ",end="")
    print()