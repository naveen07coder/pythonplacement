#Given an array nums of integers, return how many of them contain an even number of digits.

# Input: nums = [12,345,2,6,7896]
# Output: 2
# Explanation:
# 12 contains 2 digits (even number of digits).

nums = [12, 345, 2, 6, 7896]

l = []

for i in range(len(nums)):
    p = nums[i]
    l.append(str(p))

result = []
for j in range(len(l)):
    k = len(l[j])
    if (k%2 == 0):
        result.append(k)

print(len(result))