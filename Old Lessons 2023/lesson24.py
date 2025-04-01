# Food Item Class:
# You will need to create a FoodItem class with the following attributes and methods:

# Attributes:
# name: The name of the food item.
# description: A brief description of the food item.
# price: The price of the food item.
# Methods:
# __init__(self, name, description, price): Constructor method to initialize a food item with name, description, and price.
# get_name(self): Method to get the name of the food item.
# get_description(self): Method to get the description of the food item.
# get_price(self): Method to get the price of the food item.
# update_price(self, new_price): Method to update the price of the food item.
# update_description(self, new_description): Method to update the description of the food item.

# Food Management System Class:
# You will also need to create a FoodManagementSystem class with the following functionalities:

# Attributes:
# food_items: A list to store all food items.
# Methods:
# __init__(self): Constructor method to initialize an empty list of food items.
# add_food_item(self, food_item): Method to add a new food item to the system.
# remove_food_item(self, name): Method to remove a food item from the system by name.
# search_food_by_name(self, name): Method to search for a food item by name and return its details.
# update_food_price(self, name, new_price): Method to update the price of a food item.
# update_food_description(self, name, new_description): Method to update the description of a food item.
# list_all_food_items(self): Method to list all food items in the system.

class FoodItem:
    # initialise
    def __init__(self, name, price, description):
        self.name = name
        self.price = price
        self.description = description

    def get_name(self):
        return self.name

    def get_description(self):
        return self.description

    def get_price(self):
        return self.price

    def update_price(self, new_price):
        self.price = new_price

    def update_description(self, new_description):
        self.description = new_description

class FoodManagementSystem:
    def __init__(self):
        self.food_items = []

    def add_food(self, food_item):
        self.food_items.append(food_item)

    def remove_food(self, name):
        for food_item in self.food_items:
            if food_item.get_name() == name:
                self.food_items.remove(food_item)
                return

    def search_food(self, name):
        for food_item in self.food_items:
            if food_item.get_name() == name:
                return food_item
        return None # this is a null value so nothing is returned

    def update_food_price(self, name, new_price):
        food_item = self.search_food(name)
        if food_item:
            food_item.update_price(new_price)

    def update_food_description(self, name, new_description):
        for food_item in self.food_items:
            if food_item.get_name() == name:
                food_item.update_description(new_description)

    def list_all_food(self):
        for food_item in self.food_items:
            # print(food_item)
            print(f"Name: {food_item.get_name()}")
            print(f"Description: {food_item.get_description()}")
            print(f"Price: {food_item.get_price()}")
            print()

# apples = FoodItem("Apples", 2.99, "Fresh granny smith apples")
# oranges = FoodItem("Oranges", 3.99, "Fresh oranges from Spain")
# salad = FoodItem("Salad", 6.49, "Mixed greens with dressing")
# sandwich = FoodItem("Sandwich", 5.99, "Ham & cheese sandwich")

# foodsys = FoodManagementSystem()

# foodsys.add_food(apples)
# foodsys.add_food(oranges)
# foodsys.add_food(salad)

# print("List of food items in system:")
# foodsys.list_all_food()

# foodsys.update_food_price("Oranges", 1.99)
# foosys.update_food_description("Apples", "Fresh red apples from Australia")
# foodsys.remove_food("Salad")
# foodsys.add_food(sandwich)

# print("List of food items in system (AFTER UPDATES):")
# foodsys.list_all_food()

# testlist = [1, 1, 2, 4, 6, 7, 7, 9, 10]
# print(testlist)
# testset = set(testlist)
# print(testset)
# {}
# student_scores = {"Alice": 85, "Bob": 90, "Charlie": 75, "David": 88, "Emma": 92}
# print(student_scores)
# student_scores["Emma"] = 82
# student_scores["Alice"] = 95
# student_scores["Jacky"] = 77
# print(student_scores)

marcus_fruits = {"apple", "banana", "oranges", "grapes"}
shop = {"apple"}
leannes_fruits = {"banana", "mango", "blueberries", "grapes"}

common_fruits = marcus_fruits.intersection(leannes_fruits)
all_fruits = marcus_fruits.union(leannes_fruits)
differences = marcus_fruits.symmetric_difference(leannes_fruits)
# print("All fruits", all_fruits)
# print("Common favourite fruits", common_fruits)
# print("Differences", differences)

if shop.issubset(marcus_fruits):
    print("Marcus's favourite fruit is sold here")
else:
    print("Marcus's favourite fruit is not sold here")