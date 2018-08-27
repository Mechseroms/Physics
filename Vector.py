import math
import random


class PyVector(object):
    def __init__(self, x=0, y=0):
        self.x, self.y = x, y
        self.state = 0