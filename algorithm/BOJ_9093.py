N = int(input())

for i in range(N):
    str_array = input().split(" ")
    for text in str_array:
        print(text[::-1], end=" ")
    print()
