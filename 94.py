def calculate(number):
    p , s = 1, 0
    for digit in number:
        p *= int(digit)
        s += int(digit)
        return p , s
    
for number in range(100, 1000):
    p, s = calculate(number)
    if p % s == 0:
        print(number)
