# import math

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def distance_to(self, other):
#         return math.sqrt((self.x - other.x) ** 2 + (self.y - other.y) ** 2)

#     def move(self, dx, dy):
#         self.x += dx
#         self.y += dy


# p1 = Point(1, 2)
# p2 = Point(3, 4)
# print(p1.distance_to(p2))
# p2.move(2, 1)
# print("The new coordinates of p2:", p2.x, p2.y)

# name: representing the name of the product (a string).
# price: representing the price of the product (a float).
# quantity: representing the quantity of the product available (an integer).
# Implement the following methods in the Product class:

# get_details(): Return a string containing all the details of the product, formatted as "Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}".
# sell(units): Update the quantity of the product after selling the given number of units.

# class Product:
#     def __init__(self, name, price, quantity):
#         self.name = name
#         self.price = price
#         self.quantity = quantity

#     def get_details(self):
#         return f"Product: {self.name}, Price: {self.price}, Quantity: {self.quantity}"

#     def sell(self, units):
#         # taking away from the quantity, you also need to make sure you cant go negative
#         if units <= self.quantity:
#             self.quantity -= units
#             # print(f"New quantity of {self.name} is now {self.quantity}")
#             return True
#         else:
#             # print("Not enough quantity available")
#             return False

#     def restock(self, units):
#         # adding to quantity
#         self.quantity += units
#         print(f"New quantity of {self.name} is now {self.quantity}")

# class Receipt:
#     def __init__(self):
#         self.products = []

#     def add_product(self, product, quantity=1):
#         if product.sell(quantity):
#             self.products.append((product, quantity))
#         else:
#             print("Not enough quantity available")

#     def calculate_total(self):
#         total = 0
#         for product, quantity in self.products:
#             total += product.price * quantity
#         return total
    
#     def generate_receipt(self):
#         print("Receipt:")
#         for product, quantity in self.products:
#             print(f"{product.name} - Quantity: {quantity}")
#         print("Total:", self.calculate_total())

# # possible extensions discounts if you buy more than 1, points system for buying products
# # remove product

# product1 = Product("Book", 100.00, 300)
# product2 = Product("Cars", 15.00, 500)
# product3 = Product("Apple", 2.00, 200)
# product4 = Product("Carrots", 0.80, 1000)

# test_receipt = Receipt()
# test_receipt.add_product(product2, 50)
# test_receipt.add_product(product1)
# test_receipt.add_product(product3, 10)

# test_receipt.generate_receipt()

# print(product2.get_details())


# class Book:
#     def __init__ (self, title, author, price):
#         self.title = title
#         self.author = author
#         self.price = price

#     def print_details(self):
#         print("Title:", self.title, "Author:", self.author, "Price:", self.price)

# class Bookstore:
#     def __init__(self):
#         self.books = []

#     def add_book(self, new_book):
#         self.books.append(new_book)

#     def print_all_books(self):
#         print("Books in bookstore:")
#         for book in self.books:
#             book.print_details()

#     def search_book(self, title):
#         for book in self.books:
#             if book.title == title:
#                 return book
#         return False

class Car:
    def __init__(self, make, model, year, price):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def get_details(self):
        return f"Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price}"

class CarShowroom:
    def __init__(self):
        self.inventory = []

    def add_car(self, new_car):
        self.inventory.append(new_car)

    def remove_car(self, delete_car):
        if delete_car in self.inventory:
            self.inventory.remove(delete_car)

    def search_car(self, make, model):
        for car in self.inventory:
            if car.make == make and car.model == model:
                print("Car found!")
                return
        print ("Car not found!")

    def print_all_cars(self):
        print("Inventory:")
        for car in self.inventory:
            print(car.get_details())


car1 = Car("Toyota", "Camry", 2022, 25000)
car2 = Car("Honda", "Civic", 2019, 19000)

car_showroom = CarShowroom()
car_showroom.add_car(car1)
car_showroom.add_car(car2)
car_showroom.print_all_cars()
car_showroom.search_car("Honda", "Civic")
car_showroom.remove_car(car1)
car_showroom.search_car("Toyota", "Camry")
car_showroom.print_all_cars()




# 3. Design a Python class called Car to represent a car object. The Car class should have the following attributes:

# make: representing the make of the car (e.g., Toyota, Honda).
# model: representing the model of the car (e.g., Camry, Civic).
# year: representing the manufacturing year of the car.
# price: representing the price of the car.

# Additionally, implement a method in the Car class called get_details() which returns a string containing all the details of the car, formatted as "Make: {self.make}, Model: {self.model}, Year: {self.year}, Price: {self.price}"

# Next, design a Python class called CarShowroom to represent a car showroom. The CarShowroom class should have the following methods:

# add_car(car): Add a car object to the showroom's inventory.
# remove_car(car): Remove a car object from the showroom's inventory.
# search_car(make, model): Search for a car in the showroom's inventory based on the make and model. Return the car object if found, otherwise return None.
# print_all_cars(): Print details of all cars in the showroom's inventory. 