#####################################
#########  Dictionarie  #############
#####################################

#Create a dictionarie
students = {"Naty":26, "Jose":27, "Claire":22, "Bob":23}
print(students.keys())
#Print a data of the dictionarie
print(students["Naty"])

#Change a value of the dictionarie
students["Claire"] = 23
print(students["Claire"])

#Remove data
del students["Bob"]
print(students.keys())

#Convert dictionarie to List
con = list(students.keys())
print(con[1])

#Print all the values
print(students)

