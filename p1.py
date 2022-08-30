# nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
# Output: [1,2,2,3,5,6]
# Explanation: The acrrays we are merging are [1,2,3] and [2,5,6].
# The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1.
nums1 = [1,2,3,0,0,0]
m = 3
nums2 = [2,5,6]
n = 3
nums1[:] = sorted(nums1[:3]+nums2[:3])
print(nums1[:])



# MAX SUB ARRAY
nums = [-2,1,-3,4,-1,2,1,-5,4]

maxsub = nums[0]
curr = 0
for i in nums:
    if curr<0:
        curr = 0
    curr = curr + i
    maxsub = max(maxsub, curr)
print(maxsub)

nums1 = [1,2,2,1]
nums2 = [2]
p = []
for i in range(len(nums1)):
    if nums1[i] in nums2:
        p.append(nums1[i])
        ind = nums2.index (nums1[i])
        nums2[ind]= '_'
print(p)


def maxProfit(self, prices):
    maxprofit = 0
    l = len(prices)
    tot = 0
    pp = []
    for i in range(1, l - 1):
        for j in range(i + 1):
            buy = prices[i]
            sell = prices[j]
            tot = prices[i] - prices[j]
            if prices[i] > prices[j]:
                pp.append(tot)
            elif prices[i] < prices[j]:
                pp.append(0)
    return max(pp)
import numpy as np
from numpy import flatten
mat = [[1,2],[3,4]]
r = 2
c = 4
l = []
# Output: [[1,2,3,4]]
arr = mat.flat
s = np.reshape
p = arr.s(r,c)
print(p)


def factorial(n):

    if n == 1:
        return n
    else:
        facto =n*factorial(n-1)
        print(facto)
        return(facto)

print(factorial(5))
def numberOfSteps(self, num):
    n = 0
    out = []
    for i in range(num):
        if num % 2 == 0:
            k = num / 2
            out.append(k)
            print(k)

        elif num % 2 != 0:
            k = num - 1
            out.append(k)
            print(k)
    print(out)

num = 14

