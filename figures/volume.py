from figures.absfigure import Figure
from figures.flat import Sqare, Circle
from abc import abstractmethod
import math


class VolumeFigure(Figure):
    _name = 'Abstract volume figure'

    @abstractmethod
    def volume(self):
        pass

    def draw(self):
        pass


class Sphere(VolumeFigure):
    _name = "Sphere"

    def __init__(self, radius: int) -> None:
        self.__r = radius

    @property
    def radius(self):
        return self.__r

    @radius.setter
    def radius(self, radius):
        self.__r = radius

    def volume(self):
        return (4 * (math.pi * self.radius ** 3)) / 3

    def area(self):
        return 4 * math.pi * self.radius ** 2

    @staticmethod
    def static_volume(radius: int):
        return (4 * (math.pi * radius ** 3)) / 3

    @staticmethod
    def static_area(radius: int):
        return 4 * math.pi * radius ** 2


class Cube(VolumeFigure, Sqare):
    def __init__(self, side: int) -> None:
        super().__init__(side)

    @property
    def side(self):
        return super().side

    @side.setter
    def side(self, side: int):
        super().side = side

    def perimeter(self):
        return 3 * super().perimeter()

    @staticmethod
    def static_perimiter(side: int):
        return 3 * super().static_perimiter(side)

    def volume(self):
        return self.side ** 3

    @staticmethod
    def static_volume(side: int):
        return side ** 3

    def area(self):
        return 6 * super().area()

    @staticmethod
    def static_area(side: int):
        return 6 * super().static_area(side)


class Parallelepiped(VolumeFigure):
    def __init__(self, a: int, b: int, c: int) -> None:
        self.__a = a
        self.__b = b
        self.__c = c

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

    def area(self):
        return 2 * (self.a * self.b + self.b * self.c + self.c * self.a)

    @staticmethod
    def static_area(a: int, b: int, c: int):
        return 2 * (a * b + b * c + c * a)

    def volume(self):
        return self.a * self.b * self.c

    @staticmethod
    def static_volume(a: int, b: int, c: int):
        return a * b * c

    def diagonal(self):
        return (self.a ** 2 + self.b ** 2 + self.c ** 2) ** 0.5

    @staticmethod
    def static_diagonal(a: int, b: int, c: int):
        return (a ** 2 + b ** 2 + c ** 2) ** 0.5


class Cylinder(VolumeFigure, Circle):
    def __init__(self, radius: int, height: int) -> None:
        super().__init__(radius)
        self.__h = height

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, height: int):
        self.__h = height

    @property
    def radius(self):
        return super().radius

    @radius.setter
    def radius(self, radius: int):
        super().radius = radius

    def area(self):
        return 2 * math.pi * super().radius * (self.height + super().radius)

    @staticmethod
    def static_area(radius: int, height: int):
        return 2 * math.pi * radius * (height + radius)

    def lateral_area(self):
        return 2 * math.pi * super().radius * self.height

    @staticmethod
    def static_lateral_area(radius: int, height: int):
        return 2 * math.pi * radius * height

    def top_area(self):
        return 2 * super().area()

    @staticmethod
    def static_top_area(radius: int):
        return 2 * super().static_area(radius)

    def volume(self):
        return math.pi * self.height * super().radius ** 2

    @staticmethod
    def static_volume(radius: int, height: int):
        return 2 * math.pi * radius * height


class Cone(VolumeFigure):
    def __init__(self, radius: int, height: int) -> None:
        self.__r = radius
        self.__h = height
        self.__generatrix = Cone.static_generatrix(radius, height)

    @property
    def height(self):
        return self.__h

    @height.setter
    def height(self, height: int):
        self.__h = height

    @property
    def radius(self):
        return self.__r

    @radius.setter
    def radius(self, radius: int):
        self.__r = radius

    @property
    def generatrix(self):
        return self.__generatrix

    @staticmethod
    def static_generatrix(radius: int, height: int):
        return (radius ** 2 + height ** 2) ** 0.5

    def volume(self):
        return (math.pi * self.height * self.radius ** 2) / 3

    @staticmethod
    def static_volume(radius: int, height: int):
        return (math.pi * height * radius ** 2) / 3

    def area(self):
        return (math.pi * self.radius * self.generatrix) + (math.pi * self.radius ** 2)

    @staticmethod
    def static_area(radius: int, height: int):
        return (math.pi * radius * Cone.static_generatrix(radius, height)) + (math.pi * radius ** 2)

    def lateral_area(self):
        return math.pi * self.radius * self.generatrix

    @staticmethod
    def static_lateral_area(radius: int, height: int):
        return math.pi * radius * Cone.static_generatrix(radius, height)


class CorrectPyramid(VolumeFigure):
    def __init__(self, number_of_sides: int, side: int, hieght: int) -> None:
        self.__a = side
        self.__n = number_of_sides
        self.__bs = self._base_area()
        self.__h = hieght
        self.__apothem = self._apothem()

    @property
    def base_area(self):
        return self.__bs

    @property
    def hieght(self):
        return self.__h

    @hieght.setter
    def hieght(self, hieght: int):
        self.__h = hieght

    @property
    def side(self):
        return self.__a

    @side.setter
    def side(self, side: int):
        self.__a = side
        self.__s = self._base_area()

    @property
    def number_of_sides(self):
        return self.__n

    @number_of_sides.setter
    def number_of_sides(self, number_of_sides: int):
        self.__n = number_of_sides
        self.__s = self._base_area()

    def _apothem(self):
        return (self.hieght ** 2 + (self.side / (2 * math.tan(180 / self.number_of_sides)) ** 2)) ** 0.5

    @staticmethod
    def static_apotheme(number_of_sides: int, side: int, hieght: int):
        return (hieght ** 2 + (side / (2 * math.tan(180 / number_of_sides)) ** 2)) ** 0.5

    def _base_area(self):
        return (self.number_of_sides * self.side ** 2) / (4 * math.tan(180 / self.number_of_sides))

    @staticmethod
    def static_base_area(number_of_sides: int, side: int):
        return (number_of_sides * side ** 2) / (4 * math.tan(180 / number_of_sides))

    def volume(self):
        return (self.base_area * self.hieght) / 3

    @staticmethod
    def static_volume(number_of_sides: int, side: int, height: int):
        return (CorrectPyramid.static_base_area(number_of_sides, side) * height) / 3

    def lateral_area(self):
        return (self._apothem() * (self.side * self.number_of_sides)) / 2

    @staticmethod
    def static_lateral_area(number_of_sides: int, side: int, height: int):
        return (CorrectPyramid.static_apothemeapothem(number_of_sides, side, height) * (side * number_of_sides)) / 2

    def area(self):
        return self.base_area + self.lateral_area()

    @staticmethod
    def static_area(number_of_sides: int, side: int, height: int):
        return CorrectPyramid.static_base_area(number_of_sides, side) + CorrectPyramid.static_lateral_area(number_of_sides, side, height)
