def calculate_average(numbers):
    total = 0
    for num in numbers:
        total += num
    average = total / len(numbers)
    return average

# numbers = [10, 15, 20, 25, 30]
# result = calculate_average(numbers)
# print("The average is: ", result)

# Write a Python function called unique_elements(my_list) that takes a list as input and returns a new list containing only the unique elements in the same order as they appear in the original list.

def unique_elements(input_list):
    new_list = []
    for element in input_list:
        if element not in new_list:
            new_list.append(element)
    return new_list

# original_list = [1, 2, 2, 3, 4, 4, 5]

# unique_list = unique_elements(original_list)
# print(unique_list)

numbers = [1, 2, 3, 4, 5]
squared_numbers = []
for num in numbers:
    if num % 2 == 0:
        squared_numbers.append(num ** 2)
print(squared_numbers)

# squared_numbers = [num ** 2 for num in numbers if num % 2 == 0]
# print(squared_numbers)


mygrid =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# 123
# 456
# 789

n = len(mygrid)
m = len(mygrid[0])
