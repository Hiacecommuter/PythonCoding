"""
@classmethod : not conect to a particular instance
@staticamethod  : not really dependent on class, except that it is part of its namespace
@property : used to customize getters and setters for attribute
"""

class Circle:
    def __init__(self, radius):
        self._radius = radius

    @property
    def radius(self):     # getter()
        """Get value of radius"""
        return self._radius

    @radius.setter    
    def radius(self, value):
        """Set radius, raise error if negative"""
        if value >= 0 and isinstance(value, int | float) :
            self._radius = value
        else:
            raise ValueError("Radius must be positive")

    @property
    def area(self):   # an immutable property: properties without .setter() methods can’t be changed.
        """Calculate area inside circle"""
        return self.pi() * self.radius**2

    def cylinder_volume(self, height):
        """Calculate volume of cylinder with circle as base"""
        return self.area * height

    @classmethod
    def unit_circle(cls):
        """Factory method creating a circle with radius 1"""
        return cls(1)

    @staticmethod
    def pi():
        """Value of π, could use math.pi instead though"""
        return 3.1415926535
