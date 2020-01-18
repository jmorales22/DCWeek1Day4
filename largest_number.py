#Determines the largest number in a list

number_list = [2, 4, 22, 10, 16, 20, 55]
largest_number = number_list[0]

for num in number_list:
    if num >= largest_number:
        largest_number = num
print(largest_number)