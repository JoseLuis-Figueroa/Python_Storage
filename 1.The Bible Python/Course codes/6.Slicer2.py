#Slicer
# variable[start:end:step]

#Get user email address
email = input("What is your email address: ").strip()

#Slice our user name
user = email[:email.index("@")]

#Slice domain name. Use +1 to print after @
domain = email[email.index("@")+1:]

#Format message
output = "Your username is {} and your domain name is {}".format(user,domain)

#Display output message
print(output)
