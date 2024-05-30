#############################################
###### Main code with as and from ###########
#############################################

#Name the module with different name(mod)
import module as mod

#Call module as mod and take some values of the dictionary called person
print("{} is {} cm".format(mod.person["Name"],mod.person["Height"]))

print("")

#Import from module all the dictionary called person
from module import person

#Take the "Age" of the dictionary
print("Naty is {} years old".format(person["Age"]))
