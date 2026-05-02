n = int(input())
a = list(map(int, input().split()))
natija = []
for son in [1, 2, 3]:
    if son in a:
        natija.append(str(a.index(son) + 1))
    else:
        natija.append("-1")
print(" ".join(natija))