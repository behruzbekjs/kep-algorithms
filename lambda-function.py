sonlar = [5 , 8 , -8 , 0 , 13]
print(list(map(lambda x : x * 2 , sonlar)))
print*(list(filter(lambda x : x % 3 , sonlar)))

# filter(function, iterable) -> filter object
print(list(filter(lambda x : x % 3 == 0 , sonlar)))
students = ['Elbek' , 'Lobar' , 'Sardor' , 'Shaxzod' , 'Diyorbek']
print(list(filter(lambda  ism: ism.startswith('S') , students)))
new_list = []