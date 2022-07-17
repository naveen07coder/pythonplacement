s = "What is the solution to this problem"
k = int(input())
l = []
f = s.split()
for i in f:
    l.append(i)
p = tuple(l[:k])
m = " ".join(p)
print(m)