##############################################################################
# Multiple inheritance 2 at a class
##############################################################################
# Interfaces is when particular class makes a promise or a contract
# To provide a certain kind of behavior or capability.
from abc import ABC, abstractmethod

# Note: It is recommended to use a abstract class as Base class when use 
# multiple inheritance to avoid conflicts with attribute called the same.
# Beside use a astract class as a Base class give us flexibility to use it 
# wherever we want in different classes.
class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass

class GraphisShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass

# Circle class has multiple inheritance
class Circle(GraphisShape, JSONify):
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.1416 * (self.radius ** 2)

    # JSON is a kind of format used on JAVA.
    def toJSON(self):
        return f"{{\"Circle\" : {str(self.calcArea())} }}"


c = Circle(10)
print(c.calcArea())
print(c.toJSON())
