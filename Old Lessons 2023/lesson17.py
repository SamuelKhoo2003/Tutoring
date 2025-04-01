# 1. Write a Python function called swap_first_last(mylist) that takes a list as input and returns a new list where the first and last elements are swapped.
# e.g. this should be the expected output:
# mylist = [10, 20, 30, 40, 50]
# # Original List: [10, 20, 30, 40, 50]

# list indexing goes from 0 up to number of elements - 1
# it also goes from -1 to the the number of elements x -1
# [0, 1, 2, 3, 4] or [-5, -4, -3, -2, -1]

# # After calling swap_first_last(mylist):
# # Swapped List: [50, 20, 30, 40, 10]

def swap_first_last(mylist):
    firstelement  = mylist[0]
    lastelement = mylist[-1]
    mylist[0] = lastelement # [50, 20, 30, 40, 50]
    mylist[-1] = firstelement # [50, 20, 30, 40, 10]
    return mylist

inputlist = [10, 20, 30, 40, 50]
print(swap_first_last(inputlist))

# 2. Write a function row_averages(mygrid) that returns a list containing the average value of each row in the grid. Remember to use doubles as the average might not be a whole number! Once this is done can you try doing it for col_averages too? Where you return a list containing the average value for each column within the grid. 

def row_averages(mygrid):
    result = []
    for row in mygrid:
        average = sum(row) / len(row)
        result.append(average)
    return result

inputgrid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(row_averages(inputgrid))

# 3. Write a function multiply_grid(mygrid, factor) that takes a grid (mygrid) and a factor as input and multiplies each element in the grid by that factor.
# e.g. if mygrid is:
# 123
# 456
# 789
# and the factor inputed in 2, we should return a new list of grid:
# [[2, 4, 6], [8, 10, 12], [14, 16, 18]]

def multiply_grid(mygrid, factor):
    for i in range(len(mygrid)):
        for j in range(len(mygrid[i])):
            mygrid[i][j] *= factor
    return mygrid

print(multiply_grid(inputgrid, 2))

# for row in inputgrid:
#     for value in row:
#         print(value)

list  = [1, 2, 3, 4, 5]
int = 10
name  = "Marcus"

# think of a class as a blueprint for creating an object
class Employee:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

emp1 = Employee("Marcus", 21, "male")

# print(emp1.name)

class Movies:
    def __init__(self, title, year, genre, rating):
        self.title = title
        self.year = year
        self.genre = genre
        self.rating = rating

mov1 = Movies("Test Movie", 2021, "Action", 5)

class Car:
    def __init__(self, color, brand, model, plate_number):
        self.color = color
        self.brand = brand
        self.model = model
        self.plate_number = plate_number

car1 = Car('red', 'Ferrari', 'f8', 'ADC0503')
# print(car1.brand)

class Book:
    def __init__(self, title, author, genre, rating, status):
        self.title = title
        self.author = author
        self.genre = genre
        self.rating = rating
        self.status = status

    # function specific to class
    def display_info(self):
        print(f" Book Information - Title: {self.title}, Author: {self.author}, Genre: {self.genre}, Rating: {self.rating}")

    def borrow_book(self):
        if self.status == "Available":
            self.status = "Unavailable"
            print("Book has been borrowed")
        else:
            print("Book is currently unavailable")

testbook = Book("Percy Jackson and the Last Olympian", "Rick Riordan", "Greek Mythology", 4.5, "Available")
testbook.display_info()
testbook.borrow_book()
testbook.borrow_book()

# borrow_book(testbook)