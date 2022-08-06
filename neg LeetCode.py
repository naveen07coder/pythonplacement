# Move all negative numbers to beginning and positive to end with constant extra space
# Input: -12, 11, -13, -5, 6, -7, 5, -3, -6
# Output: -12 -13 -5 -7 -3 -6 11 6 5


arr = [ -12, 11, -13, -5, 6, -7, 5, -3, -6]
l=[]
k=[]
for i in range(len(arr)):
    if arr[i]<0:
        l.append(arr[i])
    else:
        k.append(arr[i])
print(l+k)