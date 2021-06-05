a = int(input())
a = abs(a)
b = list(str(a))
nums = []
for i in b:
    nums.append(i)
print(int(nums[0])+int(nums[-1]))