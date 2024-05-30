#####################################
#########  Travis system  ###########
#####################################
known_users=["Alice", "Bob", "Claire", "Dan", "Emma", "Naty", "Jorge"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    #Request a name and avoid problems for extra space and capital letter
    name=input("What is your name? ").strip().capitalize()

    print(known_users)
    
    if name in known_users:
        print ("Hello {}!".format(name))
        #Function lower reduce any letter to avoid capital letter
        remove = input("Would you like to be removed from the system (y/n) ").lower()

        if remove=="y":
            known_users.remove(name)
        elif remove=="n":
            print("No problem, I didn't want you leave anyway!")
            
    else:
        print("Mmmm I don't think I have met you yet {} ".format(name))
        add_me = input("Would you like to be added to the system (y/n)? ").strip().lower()
        if add_me == "y":
            known_users.append(name)
        elif add_me == "n":
            print("No worries, see you around!")
            
