a  =[21,442,41,45,562,4,14]

for i in range(len(a)):
    min_ind= i
    for j in range(i+1, len(a)):
        if a[min_ind]>a[j]:
            min_ind = j
    a[i], a[min_ind] = a[min_ind], a[i]

print(a)