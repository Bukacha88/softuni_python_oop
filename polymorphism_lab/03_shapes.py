from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def calculate_area(self):
        pass

    @abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.__radius = radius

    def calculate_area(self):
        area = math.pi * self.__radius * self.__radius
        return area

    def calculate_perimeter(self):
        perimeter = math.pi * 2 * self.__radius
        return perimeter


class Rectangle(Shape):
    def __init__(self, height, wight):
        self.__wight = wight
        self.__height = height

    def calculate_area(self):
        area = self.__height * self.__wight
        return area

    def calculate_perimeter(self):
        perimeter = 2 * (self.__height + self.__wight)
        return perimeter


circle = Circle(5)
print(circle.calculate_area())
print(circle.calculate_perimeter())
rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())