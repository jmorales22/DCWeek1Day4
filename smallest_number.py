#Determines the smallest number in a list

number_list = [2, 4, 22, 10, 16, 20, 55, 1]
smallest_number = number_list[0]

for num in number_list:
    if num <= smallest_number:
        smallest_number = num
    else:
        smallest_number = smallest_number
print(smallest_number)