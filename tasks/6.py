n = int(input())
lst = list(map(int , input().strip()))
for index in range(n):
    if (index + 1) % 2 != 0:
        print(lst[index] , end = " ")