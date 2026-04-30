n = int(input())
a = list(map(int, input().split()))
min_index = a.index(min(a))
max_index = a.index(max(a))
result = abs(max_index - min_index) - 1
print(result)    