print("Welcome to The Carnival!")
print("BIG RIDES ARE 7 TICKETS (bumper cars, carousel)")
print("SMALL RIDES ARE 3 TICKETS (slide, train ride)")
print("You have 15 tickets to spend.")


choosingRide = True

tickets = 15



while choosingRide == True:
    
    print("Which ride would you like go on?")
    rideChoice = input()

    
    if(rideChoice == "bumper cars"):
        
       
        print("Good Choice! Have a crashing time!!")
        tickets = tickets - 7
        if tickets < 3:
            print("WAIT !!! Sorry, you don't have enough tickets... BUT you can get a prize at the prize booth.")
            exit()
        print("You have %d left." %(tickets))
        print("Would you like to ride another ride?")
        answer = input()
        
        if answer == "no":
            print("GOOD-BYE")
            choosingRide = False
        

    elif(rideChoice == "carousel"):
        
        print("Great Choice! Don't fall!")
        tickets = tickets - 7
        if tickets < 3:
            print("WAIT !!! Sorry, you don't have enough tickets... BUT you can get a prize at the prize booth.")
            exit()
        print("You have %d left." %(tickets))
        print("Would you like to ride another ride?")
        answer = input()
        if answer == "no":
            print("GOOD-BYE")
            choosingRide = False
        
            


    elif(rideChoice == "slide"):
        
        print("Have Fun!")
        tickets = tickets - 3
        if tickets < 3:
            print("WAIT !!! Sorry, you don't have enough tickets... BUT you can get a prize at the prize booth.")
            exit()
        print("You have %d left." %(tickets))
        print("Would you like to ride another ride?")
        answer = input()
        if answer == "no":
            print("GOOD-BYE")
            choosingRide = False

    else:
        print("Sorry that is not an option. Pick again")




    

