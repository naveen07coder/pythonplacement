operations = ["X++","++X","--X","X--"]
x = 3
b=0
for i in operations:
    if i == 'X++' or i == "++X":
        b = x + 1
    elif i == 'X--' or i == "--X":
        b = x - 1

print(b)


