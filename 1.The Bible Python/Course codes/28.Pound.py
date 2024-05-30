########################################################
############# Object-Oriented programming ##############
########################################################

###################### Classes #########################

import random

#Create a class
class pound:

    def __init__(self, rare=False):             #Method to create a class
        self.rare = rare

        #If true the coin is rare
        if self.rare: #if self.rare == True
            self.value = 1.25
        else:
            self.value = 1.00

        #Class Values
        self.colour = "Gold"
        self.num_edges = 1
        self.diameter = 22.5 #mm
        self.thickness = 3.15 #mm
        self.heads = True

##Methods

    #This method changes the color to Greenish
    def rush(self):
        self.colour = "Greenish"

    #This method changes the head of the coin
    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    def __del__(self):
        print("Coin Spent!")

####################### Main ###########################

###Basic things about class
coin1 = pound()         #Create a coin using the class pound
print(coin1.colour)     #Print colour value
coin1.colour = "Silver" #Change the color of the coin1
print(coin1.colour)     #Print it

coin2 = pound()         #Create another coin
print(coin2.colour)     #Print it
##Note##
#The class keeps the same values as it can be seen in the coin2

print("")
print("")

###Review if the coin is rare   
coin1=pound(rare=True)  #Create a coin using the class pound and set the coin is rare
coin2=pound()           #Create a coin using the class pound and set the coin is not rare(False)

print(coin1.rare)       #Print rare status of coin1
print(coin2.rare)       #Print rare status of coin2

print(coin1.value)      #Print value of coin1
print(coin2.value)      #Print value of coin2

print("")
print("")

###Use of the methods
#Use rush method
coin3 = pound()         #Create a coin using the class pound
coin4 = pound()         #Create a coin using the class pound
print(coin3.colour)     #Print colour value
print(coin4.colour)     #Print colour value
coin3.rush()            #Change colour of coin3
print(coin3.colour)

print("")
print("")

#Use flip method
coin5 = pound()         #Create a coin using the class pound
print(coin5.heads)      #Print it
coin5.flip()            #Method to flip the coin5
print(coin5.heads)      #Print the result(True or False)

print("")
print("")

#Use del method
coin6 = pound()         #Create a coin using the class pound
print(coin6.value)      #Print the value of the coin
del coin6               #Delete the coin6
print(coin6.value)      #This will show a error because the coin6 was deleted

