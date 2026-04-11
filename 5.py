import math
n = int(input())
yigindi = 0
for i in range(1, n + 1):
    yigindi += int(math.isqrt(i))
print(yigindi)