##############################################################################
# Using the __str__ and __repr__ magic methods
##############################################################################  
# These magic methods help to represent much better the classes. They are 
# usually used to debug as the user can see the classes.
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: use the __repr__ method to return an obj representation
    def __repr__(self):
        return f"title={self.title}, author={self.author}, price={self.price}"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# Automaticaly they use the __str__ method
print(b1)
print(b2)

# The magic method is selected
print(str(b1))
print(repr(b2))