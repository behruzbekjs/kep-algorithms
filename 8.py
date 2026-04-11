n = input().strip()
if n == "0":
    print(1)
else:
    count = 0
    i = len(n) - 1
    
    while i >= 0:
        if n[i] == '0':
            count += 1
            i -= 1
        else:
            break
    print(count)