##############################################################################
# Using Abstract Base Classes to enforce class constraints
##############################################################################
# Abstract class contains one or more abstract methods
from abc import ABC, abstractmethod

class GraphisShape(ABC):
    def __init__(self):
        super().__init__()

    # Abstract method indicates there's no implementation in the base class
    # and each subclass has to override this method
    @abstractmethod
    def calcArea(self):
        pass

class Circle(GraphisShape):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.1416 * (self.radius ** 2) 

class Square(GraphisShape):
    def __init__(self, side):
        self.side = side

    def calcArea(self):
        return self.side * self.side


c = Circle(10)
print(c.calcArea())
s = Square(12)
print(s.calcArea())

