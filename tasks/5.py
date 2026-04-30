n = int(input())
lst = list(map(int , input().split()))
son = 0
for son in lst:
    if son < 30 and son % 3 == 0:
        print(son , end=" ")
    else:
        s += son