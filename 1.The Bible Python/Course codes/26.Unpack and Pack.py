#########################################################
################ Unpacking and Packing ##################
#########################################################

#########################################################
############### Unpack arguments ########################
#########################################################

################### Example 1 ###########################
#Create a List
numbers = [1,2,3,4,5]
print(numbers)

#Unpack the list at diferent arguments
#print(*numbers)

#Create a string
word = "abc"
print(word)

#Unpack the list at different letters
#print(*word)


################### Example 2 ###########################
#Create a function to do a sentence
def about(name, age, likes):
    sentence = "Meet {}! They are {} years old and they like {}".format(name, age, likes)

    return sentence

dictionary = {"name":"Jose", "age":23, "likes":"Python"}
#Unpack the dictionary. Two stars to unpack key words.
#sente = about(**dictionary)
print(sente)

#########################################################
################# Pack arguments ########################
#########################################################

################### Example 1 ###########################

#Create a function to do a adder using the pack arguments
def add(*numbers):
    total = 0
    for number in numbers:
        total = total + number
        
    return(total)

#### Main

#You can add any amount of numbers due to the pack function(*)
x = add(1,2,3,4,5,6)
print(x)

################### Example 2 ############################

#Create a function to do a dictionary using the pack arguments(keys and words)
def pack(**kwargs):
    for key, value in kwargs.items():
        print("{}:{}".format(key,value))
    
### Main

#You can add any amount of keys and values due to the pack function(**)
y = pack("Naty"="Female","Jose"="Male")
print(y)




