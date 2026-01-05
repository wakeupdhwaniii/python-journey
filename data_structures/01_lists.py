# Data Structures: lists

nums = [3, 1, 4, 1, 5]
nums.append(9)
nums.sort()

print(nums)
print("first:", nums[0])
print("slice:", nums[1:4])

# small exercise: sum without using sum()
total = 0
for n in nums:
    total += n
print("total:", total)
