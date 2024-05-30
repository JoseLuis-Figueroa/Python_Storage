##############################################################################
# Creating immutable data classes
##############################################################################
# Immutable data classes represent data that it is not going to be changed
from dataclasses import dataclass

# TODO: "The frozen" parameter makes the class immutable (unclangeable)
@dataclass(frozen=True)
class ImmutableClass:
    value1: str = "Value 1"
    value2: int = 0

    def somefunc(self, newval):
        self.value2 = newval

obj = ImmutableClass()
print(obj.value1)

# TODO: attempting to change the value of an immutable class
obj.value1 = "Another Value"

# TODO: even functions within the class can't change anything
obj.somefunc(20)