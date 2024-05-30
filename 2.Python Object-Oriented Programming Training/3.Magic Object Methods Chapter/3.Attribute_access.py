##############################################################################
# Using __getattribute__, __setattr__ and __getattr__
##############################################################################  
class Book:
    def __init__(self, title, author, price):
        super().__init__()
        self.title = title
        self.author = author
        self.price = price
        self._discount = 0.1
    
    # The __str__ magic method is used to return a user-friendly string
    # representation of the object
    def __str__(self,):
        return f"{self.title} by {self.author}, costs {self.price}"

    # TODO: __getattribute__ called when an attr is retrieved loop is created
    def __getattribute__(self, name):
        if name == "price":
            p = super().__getattribute__("price")
            d = super().__getattribute__("_discount")
            return p - (p * d)
        return super().__getattribute__(name)

    # TODO: __setattr__ called when a attribute value is set.
    # Don't set the attribute when is different type.
    def __setattr__(self, name, value):
        if name == 'price':
            if type(value) is not float:
                raise ValueError("The price attribute must be float")
        return super().__setattr__(name, value)

    # TODO: __getattr__ called when getattribute lookup fails. you can 
    # discover pretty much generate attributes on the fly with this method
    def __getattr__(self, name):
        return name + " is not here"


b1 = Book("War and Peace", "Leo Tolstoy", 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 29.95)

# __getattribute__ method is call as the price is modified. The price of the
# Book will be reduced by 10 %
b1.price = 38.95
print(b1)

# __setattr__ method is call as the price is a integer. It is going to raise
# the error. Try with interger to get the error.
b2.price = 32.2
print(b2)

# __getattr__ method gets called if __getattribute__ etheir does not exist,
# if it throws an exception or if the attribute does not actually exist.
# The attribute does not existe in this case
print(b2.chapter)