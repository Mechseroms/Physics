import math
import random


class PyVector(object):
    def __init__(self, x=0.0, y=0.0, limit=None):
        self._x, self._y = float(x), float(y)
        self._limit_x = limit
        self._limit_y = limit

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
    def limit_y(self):
        """ Get _limit_y attribute. """
        return self._limit_y

    @x.setter
    def x(self, number):
        """ Assign x a new float"""
        self._x = float(number)

    @y.setter
    def y(self, number):
        """ Assign y a new float"""
        self._y = float(number)

    @limit.setter
    def limit(self, number):
        """ Set _limit attribute to float(number). """
        self._limit_x = float(number)
        self._limit_y = float(number)

    @limit_x.setter
    def limit_x(self, number):
        """ Set _limit_x attribute to float(number). """
        self._limit_x = float(number)

    @limit_y.setter
    def limit_y(self, number):
        """ Set _limit_y attribute to float(number). """
        self._limit_y = float(number)

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
        """ Delete: set _limit attribute to default. """
        self._limit_x = None
        self._limit_y = None

    @limit_x.deleter
    def limit_x(self):
        """ Delete: set _limit_x attribute to default. """
        self._limit_x = None

    @limit_y.deleter
    def limit_y(self):
        """ Delete: set _limit_y attribute to default. """
        self._limit_y = None

    def __add__(self, other):
        """ Addition of an other PyVector into another using v3 = v1 + v2 notation."""
        self._x += other.x
        self._y += other.y
        self.limit_vector()
        return self

    def __sub__(self, other):
        """ Subtraction of an other PyVector into another using v3 = v1 - v2 notation."""
        self._x -= other.x
        self._y -= other.y
        self.limit_vector()
        return self

    def __mul__(self, number):
        """ Multiplication of a PyVector by a float(number). v3 = v1 * number"""
        self._x *= float(number)
        self._y *= float(number)
        self.limit_vector()
        return self

    def __truediv__(self, number):
        """ Division of a PyVector by a float(number). v3 = v1 / number"""
        self._x /= float(number)
        self._y /= float(number)
        self.limit_vector()
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

    def magnitude(self):
        """ return magnitude expression. """
        return float(
            math.sqrt(
                self._x ** 2 + self._y ** 2
            )
        )

    def limit_vector(self, number=None):
        """ Either limit using a passed float(number) or limit using a set _limit. """
        if isinstance(number, (int, float)):
            # limit if number is a float or integer:
            if self._x > float(number):
                self._x = float(number)
            if self._y > float(number):
                self._y = float(number)
        elif isinstance(number, (list, tuple)):
            # limit if number is a tuple or list of two numbers [x, y] or (x, y)
            if self._x > float(number[0]):
                self._x = float(number[0])
            if self._y > float(number[1]):
                self._y = float(number[1])
        elif self._limit_y and self._limit_x:
            # limit if both _limit_y and _limit_x has been defined
            if self._x > float(self._limit_x):
                self._x = float(self._limit_x)
            if self._y > float(self._limit_y):
                self._y = float(self._limit_y)
        elif self._limit_x:
            # limit if _limit_x has been defined
            if self._x > float(self._limit_x):
                self._x = float(self._limit_x)
        elif self._limit_y:
            # limit if _limit_y has been defined
            if self._y > float(self._limit_y):
                self._y = float(self._limit_y)

    def normalize(self):
        """ Normalize and return a PyVector. """
        if self.magnitude() != 0.0:
            return self / self.magnitude()

    def copy(self):
        """ Make a new PyVector with self._x and self._y. """
        return PyVector(x=self._x, y=self._y)

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