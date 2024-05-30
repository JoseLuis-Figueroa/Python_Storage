##############################################################################
# Implementing default values in data classes
##############################################################################
# Create a function to send a random number using the field function
from dataclasses import dataclass, field
import random

def price_function():
    return float(random.randrange(20, 40))

@dataclass
class Book:
    # you can define default values when attributes are declared. Note: you 
    # can not have default values following non-default values 
    title: str 
    author: str = "No Author"
    pages: int = 0
    price: float = field(default_factory=price_function)

# create some Book objects
b1 = Book("War and Peace", "Leo Tolstoy", 1225)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234)

print(b1)
print(b2)