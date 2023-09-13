import math


class Shape:
    """Базовый класс для геометрических фигур."""

    def area(self) -> float:
        """Вычисляет площадь фигуры."""
        pass


class Circle(Shape):
    """Класс, представляющий круг."""

    def __init__(self, radius: float) -> None:
        """
        Инициализирует объект круга.

        :param radius: Радиус круга.
        :type radius: float
        """
        if radius <= 0:
            raise ValueError("Радиус должен быть положительным числом")
        self.radius = radius

    def area(self) -> float:
        """Вычисляет площадь круга."""
        return math.pi * self.radius ** 2


class Triangle(Shape):
    """Класс, представляющий треугольник."""

    def __init__(self, side1: float, side2: float, side3: float) -> None:
        """
        Инициализирует объект треугольника.

        :param side1: Длина первой стороны треугольника.
        :type side1: float
        :param side2: Длина второй стороны треугольника.
        :type side2: float
        :param side3: Длина третьей стороны треугольника.
        :type side3: float
        """
        if any(side <= 0 for side in (side1, side2, side3)):
            raise ValueError(
                "Все стороны треугольника должны быть положительными числами! Проверьте правильность ввода.")
        elif max([side1, side2, side3]) > sum([side1, side2, side3]) - max([side1, side2, side3]):
            raise ArithmeticError("Соотношение сторон неверно")
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def area(self) -> float:
        """Вычисляет площадь треугольника."""
        s = (self.side1 + self.side2 + self.side3) / 2
        area = math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))
        return area

    def is_right_triangle(self) -> bool:
        """Проверяет, является ли треугольник прямоугольным."""
        sides = sorted([self.side1, self.side2, self.side3])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)
