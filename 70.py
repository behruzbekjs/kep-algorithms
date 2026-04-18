# a va b sonlarini o'qiymiz
a = int(input())
b = int(input())

# Nechtasi juftligini hisoblaydigan o'zgaruvchi
sanoq = 0

# a ni tekshiramiz
if a % 2 == 0:
    sanoq += 1

# b ni tekshiramiz
if b % 2 == 0:
    sanoq += 1

# Natijani chiqaramiz
print(sanoq)