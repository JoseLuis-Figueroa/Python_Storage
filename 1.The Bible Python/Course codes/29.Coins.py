########################################################
############# Object-Oriented programming ##############
########################################################

###################### Classes #########################

import random

#Father Class
class Coin:
    def __init__(self, rare=False, clean=True, heads=True, **kwargs):     #Constructor
        #**kwargs pack down the data
        #This for loop gets the value of key and value(Packed) of the all the dictionaries(Classes)
        for key,value in kwargs.items():
            setattr(self,key,value)     #This is going to assign all the data. For instance,
                                        #In pound, self.original_value = 1.00


        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        #Review if the coin is rare
        if self.is_rare: #if self.is_rare == True
            self.value = self.original_value*1.25
        else:
            self.value = self.original.value

        #Review If the coin is clean
        if self.is_clean: #if self.is_clean == True
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

    ##Methods
            
    #This method changes the color
    def rust(self):
        self.colour = self.rusty_colour

    
    def clean(self):
        self.colour = self.clean_colour

     #This method changes the head of the coin
    def flip(self):
        heads_options = [True,False]
        choice = random.choice(heads_options)
        self.heads = choice

    #This method delete the class(Spend coin)    
    def __del__(self):
        print("Coin Spent!")

    def __str__(self):
        if self.original_value >= 1:
            return "�{} coin".format(int(self.original_value))
        else:
            return "{}p coin".format(int(self.original_value*100))
    
####Classes####

#One pence class
class one_pence(Coin):
    
    def __init__(self):     
        #Pence data(dictionary)
        data = {
            "original_value":0.01,
            "clean_colour":"Bronze",
            "rusty_colour":"Brownish",
            "num_edges":1,
            "diameter":20.3,
            "thickness":1.52,
            "mass":3.56
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data


#two pence class
class two_pence(Coin):
    
    def __init__(self):     
        #Pence data(dictionary)
        data = {
            "original_value":0.02,
            "clean_colour":"Bronze",
            "rusty_colour":"Brownish",
            "num_edges":1,
            "diameter":25.9,
            "thickness":1.85,
            "mass":7.12
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data


#Five pence class
class five_pence(Coin):
    
    def __init__(self):     
        #Pence data(dictionary)
        data = {
            "original_value":0.05,
            "clean_colour":"Silver",
            "rusty_colour":None,
            "num_edges":1,
            "diameter":18.0,
            "thickness":1.77,
            "mass":3.25
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data

        #Polymorphism (create a same funtion in different class,but different content)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


#Ten pence class
class ten_pence(Coin):
    
    def __init__(self):     
        #Pence data(dictionary)
        data = {
            "original_value":0.10,
            "clean_colour":"Silver",
            "rusty_colour":None,
            "num_edges":1,
            "diameter":24.5,
            "thickness":1.85,
            "mass":6.50
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data

        #Polymorphism (create a same funtion in different class,but different content)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


#Twenty pence class
class twenty_pence(Coin):
    
    def __init__(self):     
        #Pence data(dictionary)
        data = {
            "original_value":0.20,
            "clean_colour":"Silver",
            "rusty_colour":None,
            "num_edges":7,
            "diameter":21.4,
            "thickness":1.7,
            "mass":5.00
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data

        #Polymorphism (create a same funtion in different class,but different content)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour

#Fifty pence class
class fifty_pence(Coin):
    
    def __init__(self):     
        #Pence data(dictionary)
        data = {
            "original_value":0.50,
            "clean_colour":"Silver",
            "rusty_colour":None,
            "num_edges":7,
            "diameter":27.3,
            "thickness":1.78,
            "mass":8.00
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data

        #Polymorphism (create a same funtion in different class,but different content)
        def rust(self):
            self.colour = self.clean_colour

        def clean(self):
            self.colour = self.clean_colour


#Pound class
class pound(Coin):

    def __init__(self):     #constructor
        #Pound data(dictionary)
        data = {
            "original_value":1.00,
            "clean_colour":"Gold",
            "rusty_colour":"Greenish",
            "num_edges":1,
            "diameter":22.5,
            "thickness":3.15,
            "mass":9.5
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data


#Pound class
class two_pound(Coin):

    def __init__(self):     #constructor
        #Pound data(dictionary)
        data = {
            "original_value":2.00,
            "clean_colour":"Gold & Silver",
            "rusty_colour":"Greenish",
            "num_edges":1,
            "diameter":28.4,
            "thickness":2.50,
            "mass":12.00
            }
        #Access to the father class(Coin) using the function super 
        super().__init__(**data)        #send and unpack the data


####################### Main ###########################

#list with all the coins
coins = [one_pence(), two_pence(), five_pence(), ten_pence(), twenty_pence(), fifty_pence(),
         pound(), two_pound()]

for coin in coins:
    arguments = [coin, coin.colour, coin.value, coin.diameter, coin.thickness,
                 coin.num_edges,coin.mass]

string = "{}-Colour:{}, value:{}, diameter(mm):{},thickness(mm):{}, number of edges:{}, mass(g):{}".format(*arguments)

