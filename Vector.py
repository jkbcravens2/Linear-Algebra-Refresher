from math import sqrt

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
        return Vector([x+y for x,y in zip(self.coordinates, v.coordinates)])
    
    def minus(self, v):
        return Vector([x-y for x,y in zip(self.coordinates, v.coordinates)])

    def scalarMultiply(self, scalar):
        return Vector([round(x * scalar, 3) for x in self.coordinates])

    def magnitude(self):
        return sqrt(sum([x ** 2 for x in self.coordinates]))
    
    def normalize(self):
        try:
            return self.scalarMultiply(1 / self.magnitude())
        except ZeroDivisionError:
            print 'Can not normalize zero vector'

    def innerProduct(self, v):
        return sum([x * y for x, y in zip(self.coordinates, v.coordinates)])

vector1 = Vector([1, 2, 3])
vector2 = Vector([3, 2, 1])

print vector1.innerProduct(vector2)
