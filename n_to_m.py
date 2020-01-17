#printing out a range of numbers that are input using the while loop

starting_number = int(input("Please enter the number you would like to start with: "))
ending_number = int(input("Please enter the number you would like to end with: "))

i = starting_number
while i < (ending_number + 1):
    print(i)
    i += 1