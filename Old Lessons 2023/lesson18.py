# 1. Write a Python function called reverse_rows(mygrid) that takes a 2D grid as input and returns a new grid where each row is reversed.
# Example:
# mygrid =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Original Grid:
# 1 2 3
# 4 5 6
# 7 8 9

# After calling reverse_rows(mygrid):
# Reversed Grid:
# 3 2 1
# 6 5 4
# 9 8 7

# def reverse_rows(inputgrid):
#     for i in range(len(inputgrid)):
#         inputgrid[i] = inputgrid[i][::-1]

# mygrid =  [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(mygrid)
# reverse_rows(mygrid)
# print(mygrid)

# 2. Design a class named person with the attributes of name, nickname and age, then can you write a sub class function called greeting which greets them and tells them their nickname and age. 
# 3. An extension is to add another sub function which checks if they are older or younger than age 21, printing 2 different outputs. 
class Pet:
    def __init__(self, name, nickname, age, pet_type):
        self.name = name
        self.nickname = nickname
        self.age = age
        self.pet_type = pet_type

    def personal_greet(self):
        print(f"{self.name} is a {self.pet_type}, he is {self.age} years old and we normally call him {self.nickname}")

class Person:
    def __init__(self, name, nickname, age):
        self.name = name
        self.nickname = nickname
        self.age = age

    def personal_greet(self):
        print(f"Hello my name is {self.name}, but you can call me {self.nickname}, I'm {self.age} years old.")

    def other_greet(self, friend_name):
        print(f"Hello {friend_name}! My name is {self.name}, but you can call me {self.nickname}.")

    def birthday(self, new_age):
        self.age = new_age
        print(f"{self.name} is now {self.age} years old.")

    def change_nickname(self, new_nickname):
        self.nickname = new_nickname
        print(f"Hello {self.name}, your new nickname is {self.nickname}.")

    def over21(self):
        if self.age >= 21:
            print(f"{self.name} is over or at 21 years old.")
        else:
            print(f"{self.name} is below 21 years old.")

# declaring a person
testperson = Person("Bobby", "Bob", 20)
testpet = Pet("Clifford", "Cliff", 2, "dog")

# initial checks and greetings
# testperson.personal_greet()
# testpet.personal_greet()
# testperson.over21()
# # testperson.other_greet("Alice")

# # changing variables/traits of the person
# testperson.change_nickname("BOB")
# testperson.birthday(21)

# # new checks and greetings
testperson.personal_greet()
testperson.other_greet("Alice")
# testperson.over21()

class BankAccount:
    def __init__(self, holder, balance, account_type):
        self.holder = holder
        self.balance = balance
        self.account_type = account_type

    def change_account_type(self, new_account_type):
        self.account_type = new_account_type
        print(f"The new account type is {self.account_type}")

    def deposit(self, amount):
      print(f"Your old balance was {self.balance}")
      self.balance += amount
      print(f"You have added {amount} to your account, your new balance is now {self.balance}")

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from the account, new balance is {self.balance}")
        else:
            print("Insufficient funds, withdrawal not allowed.")

    def display_info(self):
        print(f"Account Information - Holder: {self.holder}, Balance: {self.balance}, Account Type: {self.account_type}")

account1 = BankAccount("John Doe", 1000, "Savings")
account1.display_info()
account1.withdraw(1200)
account1.deposit(500)
account1.change_account_type("High Yield Savings")
account1.withdraw(1200)
account1.display_info()