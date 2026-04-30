# Return function
def sum_list(lst):
    s = 0
    for element in lst:
        s += element
        
    return s

# flexible (moslashuvchan function)


# # Amaliyot
# # 1.
# def multiply(*numbers):
#     k = 1
#     for num in numbers:
#         k *= num
#     return k
# print(multiply(2, 2))    
# # 2.
# s = 0
# def student_info(username , lastname , age):
#     for element in username , lastname , age:
#         s += element
        
#     return s
# print(student_info(2 , 4 , 7))

def find_max(*numbers):
    if len(numbers) == 0:
        return None
    
    eng_katta = numbers[0]
    
    for son in numbers:
        if son > eng_katta:
            eng_katta = son
    return eng_katta

print(find_max(4, 8, 2, 10, 6))  
print(find_max(-5, -2, -10))     
print(find_max())                