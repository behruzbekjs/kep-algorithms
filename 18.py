# n = int(input())
# natija = []
# for i in range(1, n + 1):
#     for _ in range(i):
#         natija.append(str(i))

# print(" ".join(natija))


# n = int(input())
# natija = []
# for i in range(1, n):
#     for _ in range(i):
#         natija.append(str(i))
# natija.append(str(n))
# print(" ".join(natija))


# 1. n sonini kiritamiz
n = int(input())
natija = []
for i in range(1, n):
    for _ in range(i):
        natija.append(str(i))
natija.append(str(n))
print(" ".join(natija))