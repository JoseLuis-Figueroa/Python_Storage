####################################################
################## Delete a file ###################
####################################################

#It is necessary to import the OS module to use os.remove() function
import os

#os.remove() function removes the file
os.remove("Newfile.txt")

#Check if the RemoveFile exist and delete it
if os.path.exists("RemoveFile.txt"):
    os.remove("RemoveFile.txt")
else:
    print("The file does not exist")

