n = int(input())
massiv = list(map(int, input().split()))
eng_kichik = min(massiv)
s = massiv.index(eng_kichik) + 1
print(s)