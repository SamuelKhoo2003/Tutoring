# ### **Motorcycle Class Homework**  

# #### **Objective:**  
# Create a `Motorcycle` class in Python that models the basic attributes and behaviors of a motorcycle. Your class should include:  

# - An initializer (`__init__` method) to set up a motorcycle's attributes.  
# - Methods for controlling the motorcycle (e.g., starting, stopping, accelerating, braking, checking fuel level).  
# - A method to display motorcycle details.  

# ---

# ### **Tasks:**  

# #### **1. Define the `Motorcycle` Class**  
# Create a class named `Motorcycle` with the following attributes:  
# - `make` (**str**) → The brand of the motorcycle (e.g., `"Yamaha"`)  
# - `model` (**str**) → The model of the motorcycle (e.g., `"YZF-R3"`)  
# - `year` (**int**) → The year the motorcycle was manufactured  
# - `color` (**str**) → The color of the motorcycle  
# - `speed` (**int**, default = `0`) → The current speed of the motorcycle  
# - `fuel_level` (**int**, default = `100`) → The fuel level (0-100)  

# ---

# #### **2. Implement the Following Methods:**  
# - `start_engine()` → Prints `"The engine is now running."`  
# - `stop_engine()` → Prints `"The engine is off."` and sets speed to `0`.  
# - `accelerate(amount)` → Increases speed by `amount` and prints the new speed.  
# - `brake(amount)` → Decreases speed by `amount` but doesn’t go below `0`.  
# - `refuel(amount)` → Increases fuel level by `amount`, but it cannot exceed `100`.  
# - `get_info()` → Returns a formatted string with motorcycle details.  

# ---

class Motorcycle:
    def __init__(self, make, model, year, colour, speed=0, fuel=100):
        self.make = make
        self.model = model
        self.year = year
        self.colour = colour
        self.speed = max(speed, 0)
        self.fuel = max(fuel, 0)

    def get_info(self):
        return f"This motorcycle is a {self.make} {self.model} made in {self.year} and it is {self.colour}."

    def get_speed_fuel(self):
        return f"The {self.make} is travelling at {self.speed} km per hour with {self.fuel} fuel left."

    def accelerate(self, amount):
        self.speed += amount

    def brake(self, amount):
        self.speed -= amount
        self.speed = max(self.speed, 0)

    def use_fuel(self, amount):
        self.fuel -= amount
        self.fuel = max(self.fuel, 0)

    def add_fuel(self, amount):
        self.fuel += amount
        self.fuel = min(self.fuel, 100)

def main():
    # m1 = Motorcycle("BMW", "S1000R", 2018, "white")
    # m2 = Motorcycle("Yamaha", "R1", 2015, "blue", 50, 75)
    # print(m2.get_info())
    # print(m1.get_info())
    # m1.accelerate(20)
    # m2.accelerate(30)
    # print(m1.get_speed_fuel())
    # print(m2.get_speed_fuel())
    # print(m1.get_speed_fuel())
    # m1.accelerate(20)
    # m1.use_fuel(5)
    # print(m1.get_speed_fuel())
    # m1.brake(10)
    # m1.use_fuel(10)
    # print(m1.get_speed_fuel())
    # m1.add_fuel(5)
    # print(m1.get_speed_fuel())
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print(len(numbers))
    print(sum(numbers))
    print(numbers[5])
    numbers.append(20)
    print(numbers)
    numbers.pop(5)
    print(numbers)
    print(numbers[2:5])



# if __name__ == "__main__":
main()