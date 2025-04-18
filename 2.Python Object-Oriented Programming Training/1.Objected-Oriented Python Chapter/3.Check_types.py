##############################################################################
# Checking class types and instances
##############################################################################

class Book:
    def __init__(self, title):
        self.title = title

class Newspaper:
    def __init__(self, name):
        self.name = name
    
# Create some instances of the classes
b1 = Book("The Lord of the Rings")
b2 = Book("The Secret")
n1 = Newspaper("The Washington Post")
n2 = Newspaper("The New York Times")

# TODO: use type() to inspect the object type
print(type(b1))
print(type(n2))

# TODO: compare two types together 
print(type(b1)==type(b2))
print(type(b1)==type(n1))

# TODO: use isinstance to compare a specific instance to a known type
print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(b1, Newspaper))
print(isinstance(n2, object))
