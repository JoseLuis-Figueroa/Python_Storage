####################################################
############# Write or Create a file ###############
####################################################

#Use append(A)to add a new line
f2 = open("WriteFile.txt","a")
#Use write function to add a new line
f2.write("The file has one more line!")

#Use write(w) to create a file or delete the content of an exist one
f3 = open("Newfile.txt", "w")
