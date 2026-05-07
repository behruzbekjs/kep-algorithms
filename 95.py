n = int(input())
s = 0

for i in range(n):
    son = int(input())
    if son % 2 != 0:
        s = s + son

print(s)