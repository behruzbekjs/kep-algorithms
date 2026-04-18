import math
a = float(input())
b = float(input()) 
d = math.sqrt(a**2 - 4*b)
x = (a + d) / 2
y = (a - d) / 2
print(x, y)