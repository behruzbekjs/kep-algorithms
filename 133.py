# 133
def kwargv(**kwargs):
    return len(kwargs)
print(kwargv(a = 2, b = 4, c = "a", d = None)) 
print(kwargv())                        