####################################
############## For 2 ###############
####################################
students = {
    "male":["Jose","Tom","Harry","Frank"],
    "female":["Naty","Huda","Samantha","Emily","Elizabeth"]
    }

# students.keys() send the names of male and after for female to key
for key in students.keys():
    # students[key] takes a name of the list of male and after female and send to name variable
    for name in students[key]:
        if "a" in name:
            print(name)
