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