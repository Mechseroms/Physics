import math
import random


class PyVector(object):
    def __init__(self, x=0.0, y=0.0, limit=(None, None)):
        self._x, self._y = float(x), float(y)
        self._limit_x = list(limit)
        self._limit_y = list(limit)

    def __repr__(self):
        return f"PyVector(x={self._x}, y={self._y})"

    def __str__(self):
        return f"Vector object with x: {self._x}, y: {self._y}."

    @property
    def x(self):
        """Get _x attribute"""
        return self._x

    @property
    def y(self):
        """Get _y attribute"""
        return self._y

    @property
    def limit(self):
        """ Get _limit_x and _limit_y attributes. """
        return self._limit_x, self._limit_y

    @property
    def limit_x(self):
        """ Get _limit_x attribute. """
        return self._limit_x

    @property
    def limit_x_maximum(self):
        """ Get _limit_x attribute. """
        return self._limit_x[0]

    @property
    def limit_x_minimum(self):
        """ Get _limit_x attribute. """
        return self._limit_x[1]

    @property
    def limit_y(self):
        """ Get _limit_y attribute. """
        return self._limit_y

    @property
    def limit_y_maximum(self):
        """ Get _limit_y attribute. """
        return self._limit_y[0]

    @property
    def limit_y_minimum(self):
        """ Get _limit_y attribute. """
        return self._limit_y[1]

    @x.setter
    def x(self, number):
        """ Assign x a new float"""
        self._x = float(number)

    @y.setter
    def y(self, number):
        self._y = float(number)

    @limit.setter
    def limit(self, number):
        if isinstance(number, (int, float)):
            self._limit_x[0] = float(number)
            self._limit_x[1] = float(number)
            self._limit_y[0] = float(number)
            self._limit_y[1] = float(number)
        elif isinstance(number, (tuple, list)):
            self._limit_x[0] = float(number[0])
            self._limit_x[1] = float(number[1])
            self._limit_y[0] = float(number[0])
            self._limit_y[1] = float(number[1])

    @limit_x.setter
    def limit_x(self, number):
        if isinstance(number, (int, float)):
            self._limit_x[0] = float(number)
            self._limit_x[1] = float(number)
        elif isinstance(number, (list, tuple)):
            self._limit_x[0] = float(number[0])
            self._limit_x[1] = float(number[1])

    @limit_x_maximum.setter
    def limit_x_maximum(self, number):
        if isinstance(number, (int, float)):
            self._limit_x[0] = float(number)

    @limit_x_minimum.setter
    def limit_x_minimum(self, number):
        if isinstance(number, (int, float)):
            self._limit_x[1] = float(number)

    @limit_y.setter
    def limit_y(self, number):
        if isinstance(number, (int, float)):
            self._limit_y[0] = float(number)
            self._limit_y[1] = float(number)
        elif isinstance(number, (tuple, list)):
            self._limit_y[0] = float(number[0])
            self._limit_y[1] = float(number[1])

    @limit_y_maximum.setter
    def limit_y_maximum(self, number):
        if isinstance(number, (int, float)):
            self._limit_y[0] = float(number)

    @limit_y_minimum.setter
    def limit_y_minimum(self, number):
        if isinstance(number, (int, float)):
            self._limit_y[1] = float(number)

    @x.deleter
    def x(self):
        """ Delete: set x attribute to default."""
        self._x = 0.0

    @y.deleter
    def y(self):
        """ Delete: set y attribute to default."""
        self._y = 0.0

    @limit.deleter
    def limit(self):
        self._limit_x = [None, None]
        self._limit_y = [None, None]

    @limit_x.deleter
    def limit_x(self):
        self._limit_x = [None, None]

    @limit_x_maximum.deleter
    def limit_x_maximum(self):
        self._limit_x[0] = None

    @limit_x_minimum.deleter
    def limit_x_minimum(self):
        self._limit_x[1] = None

    @limit_y.deleter
    def limit_y(self):
        self._limit_y = [None, None]

    @limit_y_maximum.deleter
    def limit_y_maximum(self):
        self._limit_y[0] = None

    @limit_y_minimum.deleter
    def limit_y_minimum(self):
        self._limit_y[1] = None

    def __add__(self, other):
        """ Addition of an other PyVector into another using v3 = v1 + v2 notation."""
        self._x += other.x
        self._y += other.y
        self.test_limit()
        return self

    def __sub__(self, other):
        """ Subtraction of an other PyVector into another using v3 = v1 - v2 notation."""
        self._x -= other.x
        self._y -= other.y
        self.test_limit()
        return self

    def __mul__(self, number):
        """ Multiplication of a PyVector by a float(number). v3 = v1 * number"""
        self._x *= float(number)
        self._y *= float(number)
        self.test_limit()
        return self

    def __truediv__(self, number):
        """ Division of a PyVector by a float(number). v3 = v1 / number"""
        self._x /= float(number)
        self._y /= float(number)
        self.test_limit()
        return self

    def __eq__(self, other):
        """ Return whether others attributes equals this vectors attributes using, v1 == v2"""
        if self._x == other.x and self._y == other.y:
            return True
        else:
            return False

    def __neg__(self):
        """ return new PyVector with x and y being made negative."""
        return PyVector(x=-self._x, y=-self._y)

    def __pos__(self):
        """ return new PyVector with x and y being made positive."""
        return PyVector(x=+self._x, y=+self._y)

    def __iadd__(self, other):
        return self.__add__(other)

    def __isub__(self, other):
        return self.__sub__(other)

    def __imul__(self, number):
        return self.__mul__(number)

    def __itruediv__(self, number):
        return self.__truediv__(number)

    def magnitude(self):
        """ return magnitude expression. """
        return float(
            math.sqrt(
                self._x ** 2 + self._y ** 2
            )
        )

    def test_limit(self):
        # set Maxes
        if self._limit_x[0]:
            # X Max
            if self._x > float(self._limit_x[0]):
                self._x = float(self._limit_x[0])
        if self._limit_x[1]:
            # X Min
            if self._x < float(self._limit_x[1]):
                self._x = float(self._limit_x[1])

        if self._limit_y[0]:
            # Y Max
            if self._y > float(self._limit_y[0]):
                self._y = float(self._limit_y[0])
        if self._limit_y[1]:
            # Y Min
            if self._y < float(self._limit_y[1]):
                self._y = float(self._limit_y[1])

    def limit_vector(self, maximum=None, minimum=None):
        """ Either limit using a passed float(maximum) or limit using a set _limit. """
        if isinstance(maximum, (int, float)):
            # limit if maximum is a float or integer:
            self._limit_x[0] = float(maximum)
            self._limit_y[0] = float(maximum)
        elif isinstance(maximum, (list, tuple)):
            # limit if maximum is a tuple or list of two numbers [x, y] or (x, y)
            self._limit_x[0] = float(maximum[0])
            self._limit_y[0] = float(maximum[1])

        if isinstance(minimum, (int, float)):
            self._limit_x[1] = float(minimum)
            self._limit_y[1] = float(minimum)
        elif isinstance(minimum, (list, tuple)):
            # limit if maximum is a tuple or list of two numbers [x, y] or (x, y)
            self._limit_x[1] = float(minimum[0])
            self._limit_y[1] = float(minimum[1])

    def normalize(self):
        """ Normalize and return a PyVector. """
        if self.magnitude() != 0.0:
            return self / self.magnitude()

    def copy(self):
        """ Make a new PyVector with self._x and self._y. """
        return PyVector(x=self._x, y=self._y)

    def convert(self):
        # TODO: this is for easy conversion for positioning using Pygame how to handle?
        return int(self._x), int(self._y)

    @staticmethod
    def add_vectors(vector_1, vector_2):
        """Static: Add two vectors and return a vector with those added attributes."""
        if isinstance(vector_1, PyVector) and isinstance(vector_2, PyVector):
            return PyVector(x=vector_1.x + vector_2.x, y=vector_1.y + vector_2.y)

    @staticmethod
    def subtract_vectors(vector_1, vector_2):
        """Static: Subtract two vectors and return a vector with those added attributes."""
        if isinstance(vector_1, PyVector) and isinstance(vector_2, PyVector):
            return PyVector(x=vector_1.x - vector_2.x, y=vector_1.y - vector_2.y)

    @staticmethod
    def random_PyVector(width, height):
        x = random.uniform(0, width)
        y = random.uniform(0, height)
        return PyVector(x=x, y=y)