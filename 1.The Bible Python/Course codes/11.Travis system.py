#####################################
#########  Travis system  ###########
#####################################
known_users=["Alice", "Bob", "Claire", "Dan", "Emma", "Naty", "Jorge"]
print(len(known_users))

while True:
    print("Hi! My name is Travis")
    #Request a name and avoid problems for extra space and capital letter
    name=input("What is your name? ").strip().capitalize()

    if name in known_users:
        print("Name recognised")
    else:
        print("Name not recognised")
