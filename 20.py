n = input()
while len(n) > 1:
    s = 0
    for raqam in n:
        s += int(raqam)
    n = str(s)
print(n)