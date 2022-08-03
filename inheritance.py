class Polygon:

    __width = None
    __heigth = None
    def setvalue(self, width, height):
        self.__width = width
        self.__heigth = height

    def get_width(self):
        return self.__width
    def get_heigth(self):
        return self.__heigth


class triangle(Polygon):
    def area(self):
        return (self.get_width()* self.get_heigth()/2)

class Rectangle(Polygon):
    def area(self):
        return self.get_heigth()*self.get_width()

rec = Rectangle()
tri = triangle()

rec.setvalue(10, 3)
tri.setvalue(10,5)
print(tri.area())

print(rec.area())
