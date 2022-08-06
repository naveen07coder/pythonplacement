A= [1, 2, 3, 4, 5]
l = []
for i in range(len(A)):
    for j in range(len(A)):
        if A[-1] == 0:
            break
        else:
            l.append(A.pop())
print(l)