#Determines the positive numbers in a given list

number_list = [2, 4, -22, 10, -16, 20, 55]
my_number = 0

for num in number_list:
    if num > my_number:
        print(num)