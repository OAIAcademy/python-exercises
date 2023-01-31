# 1 - Create a class rapresenting a point in 2d space implementing:
#               .__eq__
#               distance(self,p:point)-> float that return the distance
#               accessor for attributes
# 2 - Using the point class create a class that represent a broken line, implementing __eq__ and a .length()->float
# 3 - Using the broken line class as base, create a class representing a closed broken line
# 4 - Using the closed broken line as base create a Square class, implementing the __area__ method


# SOLUTIONS
# 1
import math


class Point:

    def __init__(self, x: float, y: float) -> None:
        super().__init__()
        self.x = x
        self.y = y

    def distance(self, p) -> float:
        assert (isinstance(p, Point))
        return math.sqrt((self.x - p.x) ** 2 + (self.y - p.y) ** 2)

    def get_x(self) -> float:
        return self.x

    def get_y(self) -> float:
        return self.y

    def set_x(self, value: float):
        self.x = value

    def set_y(self, value: float):
        self.y = value

    def __eq__(self, o: object) -> bool:
        return isinstance(o, Point) and self.x == o.x and self.y == o.y


# 2
class BrokenLine:
    def __init__(self, points: [Point]) -> None:
        super().__init__()
        self.points: [Point] = points

    def length(self) -> float:
        return sum([self.points[i].distance(self.points[i + 1]) for i in range(0, len(self.points) - 1)])

    def __eq__(self, o: object) -> bool:
        return isinstance(o, BrokenLine) \
               and len(self.points) == len(o.points) \
               and False not in [self.points[i] == o.points for i in range(0, len(self.points))]


# 3
class ClosedBrokenLine(BrokenLine):
    def __init__(self, points: [Point]) -> None:
        super().__init__(points)

    def length(self) -> float:
        return super().length() + self.points[0].distance(self.points[-1])


# 4
class Square(ClosedBrokenLine):
    def __init__(self, point_a, point_b, point_c) -> None:
        assert (point_a.distance(point_b) == point_b.distance(point_c))
        assert (abs(point_a.x - point_b.x) == abs(point_b.y - point_c.y)
                and abs(point_a.y - point_b.y) == abs(point_b.x - point_c.x))
        points = [point_a, point_b, point_c,
                  Point(x=point_c.x + (point_a.x - point_b.x), y=point_c.y + (point_a.y - point_b.y))]

        super().__init__(points)

    def __eq__(self, o: object) -> bool:
        return super().__eq__(o) and isinstance(o, Square)

    def perimeter(self) -> float:
        return self.length()

    def area(self) -> float:
        return self.points[0].distance(self.points[1]) ** 2


s = Square(Point(0, 1), Point(0, 0), Point(1, 0))
print(s.area())
print(s.perimeter())
