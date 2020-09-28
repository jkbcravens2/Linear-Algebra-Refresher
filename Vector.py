from math import *
from decimal import Decimal


class Vector(object):
    def __init__(self, coordinates):
        try:
            if not coordinates:
                raise ValueError
            self.coordinates = tuple(coordinates)
            self.dimension = len(coordinates)

        except ValueError:
            raise ValueError('The coordinates can not be empty')

        except TypeError:
            raise TypeError('Coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coordinates)

    def __eq__(self, v):
        return self.coordinates == v.coordinates

    def plus(self, v):
        return Vector([x + y for x, y in zip(self.coordinates, v.coordinates)])

    def minus(self, v):
        return Vector([x - y for x, y in zip(self.coordinates, v.coordinates)])

    def scalar_multiply(self, scalar):
        return Vector([x * scalar for x in self.coordinates])

    def magnitude(self):
        return sqrt(sum([x ** 2 for x in self.coordinates]))

    def normalize(self):
        try:
            return self.scalar_multiply(1 / self.magnitude())
        except ZeroDivisionError:
            print('Can not normalize zero vector')

    def inner_product(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

    def angle_between(self, v):
        return acos(self.inner_product(v) / (self.magnitude() * v.magnitude()))

    def is_zero(self):
        return round(self.magnitude()) == 0

    def is_parallel(self, v):
        return self.is_zero() or v.is_zero() \
               or self.angle_between(v) == 0 or self.angle_between(v) == pi

    def is_orthogonal(self, v):
        return round(self.inner_product(v)) == 0

    def project_onto(self, v):
        v_normalized = v.normalize()
        return v_normalized.scalar_multiply(self.inner_product(v_normalized))

    def orthogonal_side(self, v):
        return self.minus(self.project_onto(v))

    def cross_product(self, v):
        x1, y1, z1 = self.coordinates
        x2, y2, z2 = v.coordinates
        return Vector([y1 * z2 - y2 * z1,
                       -(x1 * z2 - x2 * z1),
                       x1 * y2 - x2 * y1])

    def area_of_parallellogram_with(self, v):
        return self.cross_product(v).magnitude()

    def area_of_triangle_with(self, v):
        return self.area_of_triangle_with(v) / Decimal('2.0')

