# True and False
animal = input("Enter your favorite animal: ")

# Condition to avoid empty string
# Empty condition will be taken as false
if animal:
	print("%s is my favorite too!" % animal)
else:
    print("You didn't write anything!")