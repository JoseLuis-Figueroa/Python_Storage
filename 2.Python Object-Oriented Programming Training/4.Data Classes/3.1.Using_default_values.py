##############################################################################
# Implementing default values in data classes
##############################################################################
# Another way to define a default values is using field function
from dataclasses import dataclass, field

@dataclass
class Book:
    # you can define default values when attributes are declared
    title: str = "No title"
    author: str = "No Author"
    pages: int = 0
    price: float = field(default=100.0)

# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)