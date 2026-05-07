def params(*args, **kwargs):
    return len(args) + len(kwargs)

print(params(2, 3, a = 2, b = 4, c = "a", d = None)) 
print(params())                              