import math

class Point:
    """Creates a point object(Euclidian)"""
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    def dist_to(self, other):
        delta_x = other.x - self.x
        delta_y = other.y - self.y
        delta_z = other.z - self.z
        return math.sqrt((delta_x)**2+(delta_y)**2+(delta_z)**2)

    def __add__(self, other):
        return Point(
            self.x + other.x,
            self.y + other.y,
            self.z + other.z
            )
    
    def __sub__(self, other):
        return Point(
            self.x - other.x,
            self.y - other.y,
            self.z - other.z
        )
