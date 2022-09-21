class Rectangle:
    def __init__(self, length, bth):
        self.__length = length
        self.__bredth = bth

    def set_length(self, length):
        self.__length = length

    def get_length(self):
        return self.__length

    def set_breath(self, bth):
        self.__bredth = bth

    def get_breath(self):
        return self.__bredth

    def area(self):
        return self.__length * self.__bredth


r1 = Rectangle(10, 22)
print(r1.get_breath())
print(r1.area())