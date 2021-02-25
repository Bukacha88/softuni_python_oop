import math


class Point:
    def __init__(self, x, y):
        self.y = y
        self.x = x

    def set_x(self, new_x):
        self.x = new_x

    def set_y(self, new_y):
        self.y = new_y

    def distance(self, x, y):
        x_dist = abs(self.x - x)
        y_dist = abs(self.y - y)
        distance = math.sqrt(x_dist * x_dist + y_dist * y_dist)
        return distance


p = Point(2, 4)
p.set_x(3)
p.set_y(5)
print(p.distance(10, 2))