##############################################################################
# Using instance methods and attributes 
##############################################################################
class Book:
    # The "init" function is called when the instance is created and ready
    # to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add propierties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def getprice(self):
        # hassattr check if an object (self=Book) has the given named atribute
        # ("_discount") and return true if present, else false
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price

    def setdiscount(self, amount):
        # The "_" tell to other developer that _discount is internal to the 
        # class and should not be access for outside of classes logic
        self._discount = amount

# TODO: create some books instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print("The price of %s is: %s" % (b1.title, b1.getprice()))

# TODO: try setting the discount
print("The price of %s is: %s" % (b2.title, b2.getprice()))
b2.setdiscount(0.25)
print("The price of %s is: %s" % (b2.title, b2.getprice()))

# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret)