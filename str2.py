words = ["pay","attention","practice","attend"]
pref = "at"

k = []
for i in range(len(words)):
    if pref in words[i]:
        k.append(words[i])
print(len(k))