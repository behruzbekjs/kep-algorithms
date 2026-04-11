n = int(input())
umumiy_kopaytma = 1
joriy_yigindi = 0
for i in range(1, n + 1):
    joriy_yigindi += i
    umumiy_kopaytma *= joriy_yigindi
print(umumiy_kopaytma)