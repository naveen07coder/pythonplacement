class sample:
    def __init__(self):
        self.a = 10
        self._b = 20
        self.__c = 30

    def public(self):
        print(self.a)
        # print(self.b)

        print(self.__privateMethods())

    # def _public(self): #cant access outside the class
    #     print(self.a)
    #     # print(self.b)

    def __privateMethods(self):
        return ("Private")


s1 = sample()
s1.public()
