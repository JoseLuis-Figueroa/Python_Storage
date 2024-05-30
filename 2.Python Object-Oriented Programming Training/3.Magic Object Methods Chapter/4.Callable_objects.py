##############################################################################
# Using the __call__ magic method
##############################################################################
# call is used when a object changes its attributes frequently or are 
# often modified together. This result in more compact code and also easy to
# read
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price

    # TODO: use the __str__ method to return a string
    def __str__(self):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: the __call__ method can be used to call the object like a function
    def __call__(self, title, author, price):
        self.title = title
        self.author = author
        self.price = price


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# TODO: Change some attributes of the class
b1.title = "Anna Karenina"
b1.price = 49.95
print(b1)

# TODO: call the object as if it were a function. Call optimaze the code 
# doing more compact and practical.
b1("War and Peace", "Leo Tolstoy", 39.95)
print(b1)