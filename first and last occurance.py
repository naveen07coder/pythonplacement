
# Given a sorted array arr containing n elements with possibly duplicate elements, the task is to find indexes of first and last occurrences of an element x in the given array.
#
# Example 1:
#
# Input:
# n=9, x=5
# arr[] = { 1, 3, 5, 5, 5, 5, 67, 123, 125 }
# Output:  2 5
# Explanation: First occurrence of 5 is at index 2 and last
#              occurrence of 5 is at index 5.


x=5
arr = [ 1, 3, 5, 5, 5, 5, 67, 123, 125 ]

p=[]
for i in range(len(arr)):
    if arr[i] == x:
        p.append(i)
print(p[0], p[-1])

