import math
n = int(input())
m = int(math.isqrt(n))
yigindi = (m * (m - 1) * (4 * m + 1)) // 6
yigindi += (n - m**2 + 1) * m
print(yigindi)