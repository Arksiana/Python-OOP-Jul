import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def set_x(self, new_x):
        self.x = new_x
        return self.x

    def set_y(self, new_y):
        self.y = new_y
        return self.y

    def distance(self, x, y):
        а = self.x - x
        b = self.y - y
        return math.sqrt(а**2 + b**2)

