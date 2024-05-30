#################################################
################### Bank ########################
#################################################

################## Classes #####################
#Father class
class Account:
    #constructor
    def __init__(self, name, balance, min_balance):     
        self.name = name
        self.balance = balance
        self.min_balance = min_balance

    #Deposit method
    def deposit(self, amount):
        self.balance += amount      #self.balance = self.balance + amount

    #Withdraw method
    def withdraw(self, amount):
        if self.balance - amount >= self.min_balance:
            self.balance -= amount  ##self.balance = self.balance - amount
        else:
            print("Sorry, not enough funds!")

    #Statement method
    def statement(self):
        print("Account balance �{}".format(self.balance))


#Classes
class Current(Account):
    def __init__(self, name, balance):
        super().__init__(name, balance, min_balance = -1000)    #Use Father class

    def __str__(self):
        return "{}'s Current Account : Balance �{}".format(self.name, self.balance)


class Saving(Account):
    def __init__(self, name, balance):
        super().__int__(name, balance, min_balance = 0)

    def __str__(self):
        return "{}'s Savings Account : Balance �{}".format(self.name, self.balance)

#################### Main ######################

account1 = Current("Jose", 500)     #Create an account using the current class
account1.deposit(300)               #Deposit 300 using method deposit
print(account1.statement())         #Print the statement
print("")

account1.withdraw(1400)             #Withdraw 1400
print(account1.statement())         #Print the statement
print("")

print(account1)                     #Print the name and balance account
print("")
print("")

account2 = Saving("Dan", 300)      #Create a saving account
print(account2)                     #Print it
account2.withdraw(301)              #Withdraw higher than the limit to receive message


