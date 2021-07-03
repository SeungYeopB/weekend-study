N = int(input())

for i in range(1,N+1):
    for j in range(0,i):
        print("*",end="")
    for j in range(0,2*N-2*i):
        print(" ",end="")
    for j in range(0,i):
        print("*",end="")
    print("")

for i in range(1,N):
    for j in range(i,N):
        print("*",end="")
    for j in range(0,2*i):
        print(" ",end="")
    for j in range(i,N):
        print("*",end="")
    print("")