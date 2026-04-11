n = int(input())
if n < 2:
    print("No")
else:
    javob = "Yes"
    i = 2
    while i * i <= n:
        if n % i == 0:
            javob = "No"
            break
        i += 1
    
    print(javob)