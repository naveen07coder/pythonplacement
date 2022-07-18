words = ["pay","attention","practice","attend"]
pref = "at"

c = 0
for i in range(len(words)):
    st=words[i]
    if(pref==st[0:len(pref)]):
        c+=1
print(c)