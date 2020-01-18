#Multiplies a factor times all of the elements in a list

number_list = [2, 4, -22, 10, -16, 20, 55]
my_number = 10
multiplied_list = []

for num in number_list:
    new_number = num * my_number
    multiplied_list.append(new_number)
print(multiplied_list)