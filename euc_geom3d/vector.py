import math
import points

class Vector:
    """Creates a vector object (Euclidian)"""
    def __init__(self, u, v, w):
        self.u = u #x component
        self.v = v #y component
        self.w = w #z component

    def __add__(self, other):
        return Vector(
            self.u + other.u,
            self.v + other.v,
            self.w + other.w
        )

    def __sub__(self, other):
        return Vector(
            self.u - other.u,
            self.v - other.v,
            self.w - other.w
        )

    