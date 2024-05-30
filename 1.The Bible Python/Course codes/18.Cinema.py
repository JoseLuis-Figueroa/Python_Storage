#####################################
############  Cinema  ###############
#####################################
films = {
    "Finding Dory":[3,5],
    "Bourne":[18,5],
    "Tarzan":[15,5],
    "Ghost Busters":[12,5]
    }

while True:
    
    choise = input("What film would you like to watch ").strip().title()

    if choise in films:
        age = int(input("How old are you?: ").strip())
        #Check user age
        if age >= films[choise][0]:
            #Check enough seats
            num_seats = films[choise][1]
            
            if num_seats > 0:
                print("Enjoy the film!")
                films[choise][1] = films[choise][1]-1
            else:
                print("Sorry, we are sold out!")
        else:
            print("You are so young to see that film!")
    
    else:
        print("We don't have that film...")
    
