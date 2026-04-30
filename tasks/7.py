n = int(input())
nums = list(map(int , input().split()))
nums.reverse()
for num in nums:
    print(num , end = " ")