i = 0
while i < (i + 1):
    print("You have " + str(i) + " coins")
    more_coins = input("Do you want another coin? (y or n) ").lower()
    if more_coins == "y":
       i += 1    
    elif more_coins == "n":
        print("Bye")
        break
    else:
        print("Please enter y or n")
