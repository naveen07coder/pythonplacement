a = [1,2,3,4,5]
b = [1,2,3]
p = set(b)
b = set(a)
k = p.union(b)
o = p.intersection(b)
print(len(set(list(k)+ list(o))))
#
#
# Given two arrays a[] and b[] of size n and m respectively. The task is to find union between these two arrays.
#
# Union of the two arrays can be defined as the set containing distinct elements from both the arrays. If there are repetitions, then only one occurrence of element should be printed in the union.