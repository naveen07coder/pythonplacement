k = []

for i in word:
    if i not in k:
        k.append(i)
p = "".join(k)
print(p)