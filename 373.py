n = int(input())
m = list(map(int , input().split()))
max_value = m[0]
for element in m:
    if element > max_value:
        max_value = element
        
print(max_value)

min_value = m[0]
for element in m:
    if element < max_value:
        max_value = element