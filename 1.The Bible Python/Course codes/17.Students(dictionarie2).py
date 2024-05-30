#####################################
#########  Dictionarie  #############
#####################################

#Create a dictionarie
students = {
            "Naty":{"id":"ID0001","age":26,"grade":"A"},
            "Jose":{"id":"ID0002","age":27,"grade":"A"},
            "Claire":{"id":"ID0003","age":22,"grade":"C"},
            "Bob":{"id":"ID0004","age":25,"grade":"D"},
            "Dan":{"id":"ID0005","age":24,"grade":"E"}
            }

#Print All
print(students)

#Print Naty age
print(students["Naty"]["age"])

#Print Dan ID
print(students["Dan"]["id"],students["Dan"]["grade"])

#Print name and grade
print(students["Naty"]["id"],students["Naty"]["age"])

#Get a Naty´s id
x = students["Naty"]["id"]
print(x)

#Change grade of Dan
students["Bob"]["grade"] = "B"
print(students["Bob"])

#Delete Dan
del students["Dan"]
print(students)
