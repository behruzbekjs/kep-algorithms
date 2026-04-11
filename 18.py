n = int(input())
for i in range(1, n + 1):
    if i == n and n != 2:
        print(i, end=" ")
    else:
        for j in range(i):
            print(i, end=" ")