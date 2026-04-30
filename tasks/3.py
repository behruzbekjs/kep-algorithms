def calculate(a, b):
    s = 0
    for i in range(a, b + 1):
        s += i
    return s
print(calculate(1, 5))  
print(calculate(5, 7))  