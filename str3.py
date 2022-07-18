s = "Myself2 Me1 I4 and3"
s = s.split()
words = [None] * len(s)

for word in s:
    w = word[:-1]
    i = int(word[-1])

    words[i - 1] = w


print(' '.join(words))

