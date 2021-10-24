from figures.absfigure import Figure
from abc import abstractmethod
import math


class FlatFigure(Figure):
    _name = 'Abstract flat figure'

    @abstractmethod
    def perimeter(self):
        pass

    def draw(self):
        pass


class Circle(FlatFigure):
    _name = 'Circle'

    def __init__(self, radius: int):
        self.__r = radius

    @staticmethod
    def static_perimiter(radius: int):
        return math.pi * radius * 2

    @staticmethod
    def static_area(radius: int):
        return math.pi * (radius ** 2)

    @property
    def radius(self):
        return self.__r

    @radius.setter
    def radius(self, radius: int):
        self.__r = radius

    @property
    def diameter(self):
        return self.radius * 2

    def area(self):
        return math.pi * (self.radius ** 2)

    def perimeter(self):
        return math.pi * self.radius * 2


class Sqare(FlatFigure):
    _name = 'Square'

    def __init__(self, side: int):
        self.__a = side

    @property
    def side(self):
        return self.__a

    @side.setter
    def side(self, side: int):
        self.__a = side

    @staticmethod
    def static_perimiter(side: int):
        return side * 4

    @staticmethod
    def static_area(side: int):
        return side ** 2

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


class Rectangle(Sqare):
    _name = 'Rectangle'

    def __init__(self, a: int, b: int):
        super().__init__(a)
        self.__b = b

    @property
    def a(self):
        return super().side

    @a.setter
    def a(self, a: int):
        super().side = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @staticmethod
    def static_perimiter(a: int, b: int):
        return (a + b) * 2

    @staticmethod
    def static_area(a: int, b: int):
        return a * b

    def sides(self):
        return (self.a, self.b)

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2


class Rhombus(Sqare):
    _name = 'Rhombus'

    def __init__(self, big_diagonal: int, short_diagonal: int):
        self.__d1 = big_diagonal
        self.__d2 = short_diagonal
        super().__init__(Rhombus.side_from_diagonals(big_diagonal, short_diagonal))

    @staticmethod
    def side_from_diagonals(big_diagonal: int, short_diagonal: int):
        return ((big_diagonal ** 2 + short_diagonal ** 2) ** 0.5) / 2

    @property
    def side(self):
        return super().side

    @property
    def big_diagonal(self):
        return self.__d1

    @big_diagonal.setter
    def big_diagonal(self, big_diagonal):
        self.__d1 = big_diagonal
        Rhombus.side_from_diagonals(big_diagonal, self.short_diagonal)

    @property
    def short_diagonal(self):
        return self.__d2

    @short_diagonal.setter
    def short_diagonal(self, short_diagonal):
        self.__d2 = short_diagonal
        Rhombus.side_from_diagonals(self.big_diagonal, short_diagonal)

    def area(self):
        return (self.big_diagonal * self.short_diagonal) * 0.5

    @staticmethod
    def static_area(big_diagonal: int, short_diagonal: int):
        return (big_diagonal * short_diagonal) * 0.5

    def perimeter(self):
        return super().perimeter()

    @staticmethod
    def static_perimiter(side: int):
        return super().static_perimiter(side)


class Trapezoid(FlatFigure):
    _name = "Trapezoid"

    def __init__(self, a: int, b: int, c: int, d: int) -> None:
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a: int):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b: int):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c: int):
        self.__c = c

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, d: int):
        self.__d = d

    def sides(self):
        return (self.a, self.b, self.c, self.d)

    def area(self):
        return ((self.a + self.b) / 2) * ((self.c ** 2 - (((self.b - self.a) \
                ** 2 + self.c ** 2 - self.d ** 2) / 2 * (self.b - self.a)) ** 2) ** 1 / 2)

    @staticmethod
    def static_area(a: int, b: int, c: int, d: int):
        return ((a + b) / 2) * ((c ** 2 - (((b - a) \
                ** 2 + c ** 2 - d ** 2) / 2 * (b - a)) ** 2) ** 1 / 2)

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    @staticmethod
    def static_perimeter(a: int, b: int, c: int, d: int):
        return a + b + c + d


class Triangle(FlatFigure):
    _name = "Triangle"

    def __init__(self, a: int, b: int, c: int) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, a):
        self.__a = a

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, b):
        self.__b = b

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, c):
        self.__c = c

    def sides(self):
        return (self.a, self.b, self.c)

    def area(self):
        return (self.perimeter() * (self.perimeter() - self.a) \
            * (self.perimeter() - self.b) * (self.perimeter() - self.c)) ** 0.5

    @staticmethod
    def geron_area(a: int, b: int, c: int):
        return (Triangle.static_perimeter(a, b, c) * (Triangle.static_perimeter(a, b, c) - a) \
            * (Triangle.static_perimeter(a, b, c) - b) * (Triangle.static_perimeter(a, b, c) - c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    @staticmethod
    def static_perimiter(a: int, b: int, c: int):
        return a + b + c
