nums = [3,4,5,2]

o = []

for i in range(len(nums)):
    for j in range(i):
        k = ((nums[i]-1)*(nums[j]-1))
        o.append(k)
print(max(o))

