for son in range(1000, 10000):
    s = str(son)
    yigindi = int(s[0]) + int(s[1]) + int(s[2]) + int(s[3])
    if yigindi % 2 == 0:
        print(son, end=" ")