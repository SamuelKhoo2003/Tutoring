# # Q1
# for i in range(3):
#     print(i)

# # Q1 Answer
# 0,1,2


# # Q2
# x = 0
# while x < 10:
#     print(x)
#     x += 2 # x = x + 2

# # Q2 Answer
# 0,2,4,6,8

# # Q3
# res = []
# for x in range(3):
#     res.append(x*2) # multiply by 2
# print(res)

# # Q3 Answer
# [0, 2, 4]


# # Q4
# print('Python'[::-1]) # -1 means reverse order

# # Q4 Answer
# 'nohtyP'


# # Q5
# print(3//2)
# print(2**3)

# # Q5 Answer
# 1
# 8

# Find me how many minutes are in a year:
def return_year_minutes(number_of_years: int) -> int:
    numOfDaysInYear = 365
    numOfHoursInDay = 24
    numOfMinutesInHour = 60
    return number_of_years * numOfDaysInYear * numOfHoursInDay * numOfMinutesInHour


print(f" There are {return_year_minutes(1)} minutes in 1 year")
print(f" There are {return_year_minutes(3)} minutes in 3 year")

# Name and Address
name = input("Given name: ")
familyname = input("Family name: ")
address = input("Address: ")
city = input("City: ")
phone_number = input("Phone Number: ")

print(f"{name} {familyname}") # print(name + " " + familyname)
print(f"{address}, {city}")
print(phone_number)


# Given name:
# Family name:
# Address:
# City:
# Phone Number:

# Samuel Khoo
# 66 Street, London
# 07785581300

# Arithmetics
def all_arithmetics(x: int, y: int):
    print(f"{x} + {y} = {x + y}")
    print(f"{x} - {y} = {x - y}")
    print(f"{x} * {y} = {x * y}")
    print(f"{x} / {y} = {x / y}")

all_arithmetics(27, 15)
all_arithmetics(36, 4)

# Float Vs Int
x = 9.93
print(f"float = {float(x)}")
print(f"int = {int(x)}")

# Food Expenditure
def food_expenditure(times: int, price: float, groceries: float):
    weekly = times*price + groceries
    daily = weekly / 7
    print("Average food expenditure")
    print(f"Daily: {round(daily, 2)} dollars")
    print(f"Weekly: {weekly} dollars")

numTimes = int(input("How many times a week do you eat at the student cafetaria? "))
foodPrice = float(input("What is the price of a typical lunch? "))
groceryCost = float(input("How much money do you spend on groceries a week? "))

food_expenditure(numTimes, foodPrice, groceryCost)


# Number Of Groups

import math

students = int(input("How many students are in this course? "))
size = int(input("Desired group size? "))

def numberOfGroups(numStudents: int, desiredSized: int) -> int:
    # Write your code here
    if numStudents <= 0 or desiredSized <= 0:
        return 0
    return int(math.ceil(numStudents /desiredSized))

print(f"Number of groups formed: {numberOfGroups(students, size)} groups")