arr  =[21,442,41,45,562,4,14]

for i in range(1, len(arr)):
    key = arr[i]
    j = i=1
    while j>=0 and key<arr[j]:
