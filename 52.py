n = int(input())
massiv = input().split()
def saralash_sharti(s):
    yigindi = sum(int(raqam) for raqam in s) 
    birinchi_raqam = int(s[0])              
    qiymati = int(s)                         
    return (yigindi, birinchi_raqam, qiymati)
massiv.sort(key=saralash_sharti)
print(*(massiv))