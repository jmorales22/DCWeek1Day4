#Determines the positive numbers in a given list and creates a new list

number_list = [2, 4, -22, 10, -16, 20, 55]
my_number = 0
positive_list = []

for num in number_list:
    if num > my_number:
        positive_list.append(num)
print(positive_list)