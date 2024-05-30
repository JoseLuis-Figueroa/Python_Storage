##############################################################################
# Implementing default values in data classes
##############################################################################
# One way to define default values
from dataclasses import dataclass

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No Author"
    pages: int = 0
    price: float = 0.0

# create some Book objects
b1 = Book()
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)