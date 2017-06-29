#grocerylist = ["strawberries", "watermelon", "milk", "chocolate", "hot cheetos"]
#for x in grocerylist:
    #print (x)
grocerylist = []
choice = True

while choice == True:
    print("Do you want to add an item to your list? (y/n)")
    answer = input()
    if (answer.upper() == "YES" or "YEAH" or "Y"):
        print("What would you like to add?")
        answer2 = input()
        grocerylist.append(answer2)  
        
    elif(answer.upper() == ("N" or "NO" or "NO THANKS")):
        break 
        
        for x in grocerylist:
            print (x)
        print ("Have a nice day! BYE.")
    
#if 
    
    
    
        
