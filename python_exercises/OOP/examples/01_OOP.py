import random


class Prova:  # definition
    statico = 'statico'  # static name

    def __init__(self, x) -> None:  # constructor
        super().__init__()
        self.x = x  # attribute x
        self.y = self.x * 2

    def method(self):  # method
        return self.x + self.y


print(Prova.statico)  # access static
prova = Prova(1)  # Instantiation
print(prova.method())  # calling a method
print(prova.y)  # accessing attributes

print(prova.__dict__)  # access underling dict


class Polygon:  # abstract class, only used as base for other class

    def __init__(self) -> None:
        pass

    def area(self):  # abstract method to be overridden
        pass

    def __eq__(self, o: object) -> bool:  # define the == operator to be overridden
        return isinstance(o, Polygon)


class Rectangle(Polygon):  # class derived from polygon
    def __init__(self, side_a_len: float, side_b_len: float) -> None:
        super().__init__()  # always call the super constructor
        self.side_a_len = side_a_len
        self.side_b_len = side_b_len

    def area(self) -> float:  # override the base area
        return self.side_a_len * self.side_b_len

    def __eq__(self, o: object) -> bool:  # check if instance rectangle and then check every attribute
        return super().__eq__(o) and isinstance(o, Rectangle) \
               and self.side_b_len == o.side_b_len \
               and self.side_a_len == o.side_a_len

    # accessor are method use to hide the implementation of attribute
    def get_side_a_len(self) -> float:
        return self.side_a_len

    def get_side_b_len(self) -> float:
        return self.side_a_len

    def set_side_a_len(self, value: float):
        self.side_a_len = value

    def set_side_b_len(self, value: float):
        self.side_a_len = value


class Square(Rectangle):
    def __init__(self, side_len: float) -> None:
        super().__init__(side_len, side_len)  # a square is a rectangle with same length side

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and isinstance(o, Square)


class Triangle(Polygon):

    def __init__(self, base: float, high: float) -> None:
        super().__init__()
        self.base = base
        self.high = high

    def area(self) -> float:  # alternative implementation of area() for the triangle
        return (self.base * self.high) / 2

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) \
               and isinstance(o, Triangle) \
               and self.base == o.base \
               and self.high == o.high


print("\n\n\n")
t = Triangle(6, 8)
s = Square(5)
print(t == s)  # using the operator == auto call __eq__
print(s == Square(5))
# create list of polygon selecting randomly the type
l: [Polygon] = []
for i in range(0, 10):
    r = random.randint(0, 3)
    if r == 0:
        l.append(Rectangle(3, 4))  # area  = 12
    elif r == 1:
        l.append(Square(2))  # area  = 4
    else:
        l.append(Triangle(1, 3))  # area  = 1.5
# the right area method is called
for p in l:
    print(p.area())
