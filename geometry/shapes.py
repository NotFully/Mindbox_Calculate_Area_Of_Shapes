import math


class Shape:
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Радиус должен быть натуральным числом")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Triangle(Shape):
    def __init__(self, side1, side2, side3):
        if any(side <= 0 for side in (side1, side2, side3)):
            raise ValueError("Все стороны треугольника должны быть положительными числами! Проверьте правильность ввода.")
        elif max([side1, side2, side3]) > sum([side1, side2, side3]) - max([side1, side2, side3]):
            raise ArithmeticError("Соотношение сторон неверно")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self):
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def is_right_triangle(self):
        sides = sorted([self.side1, self.side2, self.side3])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)
