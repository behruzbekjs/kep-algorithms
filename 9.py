for n in range(1000, 10000):
    s = str(n)
    teskari_s = s[::-1]
    teskari_n = int(teskari_s)
    if teskari_n == n * 4:
        print(n)
        break