def map(func , squence):
    new_lst = []
    for b in squence:
        new_lst.append(func(n))
        
    return new_lst
print(map(lambda x: x + 2 , [-5 , 0 , 5]))
print(map(lambda y: y + 3, [2 , 5 , 8 , 6]))