# Input: nums = [1,2,5,2,3], target = 2
# Output: [1,2]
nums = [1,2,5,2,3]
target = 2
li = []
k = sorted(nums)
for i in range(len(k)):
    if target == k[i]:
        li.append(i)

print(li)
