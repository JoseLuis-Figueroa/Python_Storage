#####################################
#########  Dictionarie  #############
#####################################

#Create a dictionarie
students = {
            "Naty":["ID0001",26,"A"],
            "Jose":["ID0002",27,"A"],
            "Claire":["ID0003",22,"C"],
            "Bob":["ID0004",25,"D"],
            "Dan":["ID0005",24,"E"]
            }

#Print all the Naty information
print(students["Naty"])

#Print only Naty ID
print(students["Naty"][0])

#Print age and grade of Jose
print(students["Jose"][1:])
