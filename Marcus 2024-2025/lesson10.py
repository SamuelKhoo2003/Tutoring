class Person:
    def __init__(self, name, age, gender):
        # its initialising the properties of a person
        self.name = name
        self.age = age
        self.gender = gender

    # introduce is something that can only be called by a person instance/class
    def introduce(self):
        return f"Hello my name is {self.name}. I'am {self.age} years old."

    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

    def change_name(self, new_name):
        self.name = new_name
        return f"Name successfully changed to {self.name}."

p = Person("Alice", 25, "Female")
p2 = Person("Bob", 31, "Male")
# print(p.introduce())
# print(p2.introduce())
# print(p2.have_birthday())
# print(p2.introduce())
# print(p2.change_name("Jack"))
# print(p2.introduce())

# build me an animal class, with traits of species, name, age, number of legs, sound
class Animal:
    def __init__(self, name, species, age, legs, sound):
        self.name = name
        self.species = species
        self.age = age
        self.legs = legs
        self.sound = sound

    def make_sound(self):
        return f"{self.name} says {self.sound}!"

    def get_info(self):
        return f"{self.name} is a {self.age}-year old {self.species} with {self.legs} legs."

    def have_birthday(self):
        self.age += 1
        return f"Happy Birthday {self.name}! You are now {self.age} years old."

a = Animal("Bob", "Cat", 15, 4, "meow")
a2 = Animal("Clifford", "Dog", 3, 4, "woof")
print(a.get_info())
print(a.have_birthday())
# print(a.make_sound())
# print(a.get_info())
# print(a2.get_info())
# print(a2.make_sound())



# print(f"{a.name} says {a.sound}!")

