nums = [0, 10]
k = 2
p = []
for i in range(len(nums)):
    l = nums[i] + k
    p.append(l)

m = (max(p)-min(p))
print(m)