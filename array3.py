nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3
o = []
p = []
for i in range(m):
    o.append(nums1[i])

for j in range(n):
    p.append(nums2[j])

print(sorted(o+p))