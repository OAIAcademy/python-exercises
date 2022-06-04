import math


def distanza_manth(point1, point2):
    return abs(point1['x'] - point2['y'])


class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b

    def distanza_da_origine(self):
        return math.sqrt(self.x ** 2 + self.y ** 2)


if __name__ == '__main__':
    point = Point(1, 2)
    print(point.x)
    point.x = 12
    print(point.distanza_da_origine())
    print(type(point))
