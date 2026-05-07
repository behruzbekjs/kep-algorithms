def filter_list(list , n):
    if n ==0:
        for odd_num in list:
            if odd_num % 2 != 0:
                list.remove(odd_num)
                return list
    else:
        for even_num in list:
            if even_num % 2 == 0:
                list.remove(even_num)
                return list
            
print(filter_list([1, 2, 3, 4, 5, 6], 0)) 
print(filter_list([3, 5, 3, 6, 1], 1))    