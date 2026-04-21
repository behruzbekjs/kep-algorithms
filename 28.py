n = int(input())
strings = []
for i in range(n):
    s = input()
    strings.append(s)

for s in strings:
    if len(s) > 10:
        print(s[0] + s[-1])
    else:
        print(s)

