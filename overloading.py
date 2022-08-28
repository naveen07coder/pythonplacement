#overloading

class Over:
    def inte(a, b):
        c = a+b
        return c
    def inte(a,b):
        c = a+b
        return c
a = Over

print(a.inte(1,2))
print(a.inte("NAVEEN", "kumar"))


#Overriding
class Over:
    def inte(a, b):
        c = a+b
        return c

class O2ver:
    def inte(a,b):
        c = a+b
        return c

    def thre(a,b,c):
        return a,b,c
a = Over
ab  = O2ver

print(a.inte(1,2))
print(ab.inte("NAVEEN", "kumar"))
print((ab.thre(12,"ahd", 13)))
print((ab.thre("ahd", 13,31)))