##############################################################################
# Data class
##############################################################################
# The classes will be represent different using Data Classes with a code much
# more concise. Besides, the Data Classes implement themself some magic 
# methods. Data Class is included on 3.7 python and later.
from dataclasses import dataclass

# the initializer (__init__) and self function are not needed   
@dataclass
class Book:
    title: str
    author: str
    pages: int
    price: float

    # method can be used as before (normal classes).
    def bookinfo(self):
        return f"{self.title}, by {self.author}"

# create some instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)
b3 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)

# access fields
print(b1.title)
print(b2.author)

# TODO: print the book itself - dataclasses implement __repr__
print(b1)

# TODO: comparing two dataclasses - they implement __eq__
print(b1 == b3)

# TODO: change some fields
b1.title = "Anna Karenina"
b1.pages = 864
print(b1.bookinfo())