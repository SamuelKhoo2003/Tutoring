# class Pet:
#     def __init__(self, name, nickname, age, pet_type):
#         self.name = name
#         self.nickname = nickname
#         self.age = age
#         self.pet_type = pet_type

#     def personal_greet(self):
#         print(f"{self.name} is a {self.pet_type}, he is {self.age} years old and we normally call him {self.nickname}")

# class Agent():
#     def __init__(self, default_currncy = 'HKD Curncy')


class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year
        self.is_started = False

    def start(self):
        self.is_started = True
        print(f"The {self.brand} {self.model} has been started.")

    def stop(self):
        self.is_started = False
        print(f"The {self.brand} {self.model} has been stopped.")

    def honk(self):
        if self.is_started:
            print(f"The {self.brand} {self.model} is honking.")
        else:
            print(f"The {self.brand} {self.model} is not started.")

    def display_info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}")

# Creating objects (instances) of the Car class
car1 = Car("Toyota", "Camry", 2022)
car2 = Car(2021, "Civic", "Honda")
car2.display_info()
# listofcars = []
# for carvalues in cartable: 
#     tmpcar = Car(carvalues[0], carvalues[1], carvalues[2])
#     listofcars.append(tmpcar)

# if currncy is None:
#     currncy = self.default_currncy
# else:
#     currncy = currncy




# Accessing object attributes and calling methods
# print(car1.brand)  # Output: "Toyota"
# print(car1.model)
# print(car1.year)
# car1.display_info()

# print(car2.year)   # Output: 2021

# car1.start()  # Output: "The Toyota Camry has been started."
# # car2.honk()   # Output: "The Honda Civic is not started."

# car1.honk()   # Output: "The Toyota Camry is honking."
# car2.stop()   # Output: "The Honda Civic has been stopped."
