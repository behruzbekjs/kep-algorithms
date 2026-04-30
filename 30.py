n = int(input())
a = list(map(int, input().split()))
res1 = -1
res2 = -1
res3 = -1
count1 = 0
for i in range(n):
    if a[i] == 1:
        count1 += 1
        if count1 == 1:
            res1 = i + 1
            break

count2 = 0
for i in range(n):
    if a[i] == 2:
        count2 += 1
        if count2 == 2:
            res2 = i + 1
            break

count3 = 0
for i in range(n):
    if a[i] == 3:
        count3 += 1
        if count3 == 3:
            res3 = i + 1
            break

print(res1, res2, res3)