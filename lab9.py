import uuid
from abc import ABC, abstractmethod

import matplotlib.pyplot as plt


class Figure(ABC):
    def __init__(self):
        self.id = str(uuid.uuid1())

    def move(self, dx, dy):
        try:
            new_coords = [(x + dx, y + dy) for x, y in self._get_coordinates()]
            self.a, self.b, self.c, self.d = new_coords[:4]  # Для Rectangle
            if isinstance(self, Pentagon):
                self.e = new_coords[4]  # Для Pentagon
        except Exception as e:
            raise RuntimeError(f"Ошибка при перемещении фигуры: {e}")

    def get_coordinates(self):
        return self._get_coordinates()

    @abstractmethod
    def _get_coordinates(self):
        return []

    @staticmethod
    def _coordinates_valid(value: tuple) -> bool:
        if isinstance(value, tuple) and len(value) == 2 and isinstance(value[0], (int, float)) and isinstance(value[1],
                                                                                                              (int,
                                                                                                               float)): return True
        return False

    def show(self, ax, color, label):
        # Получаем координаты и рисуем линии, соединяя вершины
        coords = self._get_coordinates()
        x_vals = [point[0] for point in coords]
        y_vals = [point[1] for point in coords]

        x_vals.append(x_vals[0])
        y_vals.append(y_vals[0])

        ax.plot(x_vals, y_vals, marker='o', color=color, label=label)
        for i, (x, y) in enumerate(coords):
            ax.text(x, y, f'({x}, {y})', fontsize=12, ha='right')


class Rectangle(Figure):

    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y):
        super().__init__()
        self.a = (a_x, a_y)
        self.b = (b_x, b_y)
        self.c = (c_x, c_y)
        self.d = (d_x, d_y)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__a = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__b = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__c = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__d = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    def __area(self):
        width = abs(self.b[0] - self.a[0])
        height = abs(self.d[1] - self.a[1])
        return width * height

    def _get_coordinates(self):
        return [self.a, self.b, self.c, self.d]

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.__area() == other.__area()
        return False


class Pentagon(Figure):
    def __init__(self, a_x, a_y, b_x, b_y, c_x, c_y, d_x, d_y, e_x, e_y):
        super().__init__()
        self.a = (a_x, a_y)
        self.b = (b_x, b_y)
        self.c = (c_x, c_y)
        self.d = (d_x, d_y)
        self.e = (e_x, e_y)

    @property
    def a(self):
        return self.__a

    @a.setter
    def a(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__a = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def b(self):
        return self.__b

    @b.setter
    def b(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__b = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def c(self):
        return self.__c

    @c.setter
    def c(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__c = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def d(self):
        return self.__d

    @d.setter
    def d(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__d = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    @property
    def e(self):
        return self.__e

    @e.setter
    def e(self, value: tuple):
        if Figure._coordinates_valid(value):
            self.__e = value
        else:
            raise ValueError("Value must be a tuple of length 2")

    def _get_coordinates(self):
        return [self.a, self.b, self.c, self.d, self.e]

    def __area(self):
        coords = [self.a, self.b, self.c, self.d, self.e]
        n = len(coords)
        area = 0
        for i in range(n):
            x1, y1 = coords[i]
            x2, y2 = coords[(i + 1) % n]
            area += x1 * y2 - x2 * y1
        return abs(area) / 2

    def __eq__(self, other):
        if isinstance(other, Pentagon):
            return self.__area() == other.__area()
        return False


def is_include(t1, t2):
    if isinstance(t1, Figure) and isinstance(t2, Figure):
        t1_coords = t1._get_coordinates()
        return all(is_point_in_polygon(t1_coords, point) for point in t2._get_coordinates())
    else:
        raise TypeError("Unsupported figure type for t1")


def is_point_in_polygon(polygon_coords, point):
    x, y = point
    n = len(polygon_coords)
    inside = False
    p1x, p1y = polygon_coords[0]

    for i in range(n + 1):
        p2x, p2y = polygon_coords[i % n]
        if min(p1y, p2y) <= y <= max(p1y, p2y):
            if y == p1y == p2y:
                if min(p1x, p2x) <= x <= max(p1x, p2x):
                    return True  # Point is on a horizontal edge
            elif y == p1y or y == p2y:
                y += 1e-10  # Slightly adjust y to avoid ambiguity
            else:
                xinters = (y - p1y) * (p2x - p1x) / (p2y - p1y) + p1x
                if x == xinters:
                    return True  # Point is on the edge
                if x < xinters:
                    inside = not inside
        p1x, p1y = p2x, p2y

    return inside


fig, ax = plt.subplots()

rect = Rectangle(0, 0, 6, 0, 6, 6, 0, 6)
pentagon = Pentagon(1, 1, 2, 4, 4, 4, 5, 1, 3, 0)
print(rect.get_coordinates())
print(pentagon.get_coordinates())
print(is_include(rect, pentagon))  # Should return True before moving
rect.show(ax, color='blue', label=f'Rectangle (ID: {rect.id})')
pentagon.show(ax, color='red', label=f'Pentagon (ID: {rect.id})')

ax.legend()
plt.show()
