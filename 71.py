# Sonni matn (string) ko'rinishida o'qiymiz
s = input()

# Birinchi 3 ta raqamni ajratib olamiz va yig'indisini hisoblaymiz
chap_qism = int(s[0]) + int(s[1]) + int(s[2])

# Oxirgi 3 ta raqamni ajratib olamiz va yig'indisini hisoblaymiz
ong_qism = int(s[3]) + int(s[4]) + int(s[5])

# Yig'indilar teng bo'lsa True, aks holda False chiqaramiz
print(chap_qism == ong_qism)