def sum_of_digits(number):
    s = 0
    for digit in str(number):
        raqam = int(digit)
        s += raqam 
    return s
n = input()
start = n[0 : 3]
end = n[0 : 3]
# print(start , end)
if sum_of_digits(start) == sum_of_digits(end):
    print("YES")