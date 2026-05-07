# 132
def argv_int(*args):
    count = 0
    for arg in args:
        if type(arg) is int:
            count += 1
    return count



print(argv_int(2, 4, "a", 5.0, None)) 
print(argv_int())                     