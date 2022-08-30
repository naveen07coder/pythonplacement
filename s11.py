s = "anagram"
t = "nagaram"


def isAnagram(s, t):

    s = list(s)
    t = list(t)
    ans = []
    for i in range(len(s)):
        for j in range(len(t)):
            if s[j] in t:
                ans.append(s[j])
                t.remove(s[j])
    if sorted(ans) == sorted(t):
        return True
    else:
        return False

    # ans = []
    # for i in s:
    #     if i in t:
    #         ans.append(i)
    # if ("".join(ans)) in t:
    #     return True
    # else:
    #     return False
print(isAnagram(s,t))

