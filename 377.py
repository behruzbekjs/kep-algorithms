n = int(input())
sonlar = list(map(int, input().split()))
noyob_sonlar = set(sonlar)
natija = 0
for son in noyob_sonlar:
    if sonlar.count(son) == 2:
        natija += 1
print(natija)