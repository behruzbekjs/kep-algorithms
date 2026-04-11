n = int(input())
tublar = [True] * (n + 1)
tublar[0] = tublar[1] = False # 0 va 1 tub emas
i = 2
while i * i <= n:
    if tublar[i]:
        # Agar i tub bo'lsa, uning barcha karralilarini (2i, 3i...) "tub emas" qilamiz
        for j in range(i * i, n + 1, i):
            tublar[j] = False
    i += 1
for son in range(2, n + 1):
    if tublar[son]:
        print(son, end=" ")