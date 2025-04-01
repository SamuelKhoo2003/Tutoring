class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.rented = False

    def get_car_details(self):
        return "Make: {self.make}, Model: {self.model}, Year: {self.year}, Status: {self.rented}"

class Customer:
    def __init__(self, name, customer_id):
        self.name = name
        self.customer_id = customer_id

    def get_customer_details(self):
        return f"{self.name} (ID: {self.customer_id})"

class CarRental:
    def __init__(self):
        self.car_inventory = []
        self.customer_inventory = []

    def add_car(self, car):
        self.car_inventory.append(car)

    def remove_car(self, make, model, year):
        for car in self.car_inventory:
            if car.make == make and car.model == model and car.year == year:
                self.car_inventory.remove(car)
                return
        print("Car not found in rental system")

    def add_customer(self, customer):
        self.customer_inventory.append(customer)

    def remove_customer(self, customer_id):
        for customer in self.customer_inventory:
            if customer.customer_id == customer_id:
                self.customer_inventory.remove(customer)
                return
        print("Customer not found in system")

    # function to rent a car
    def rent_car(self, customer_id, make, model):
        for car in self.car_inventory:
            if car.make == make and car.model == model and not car.rented:
                car.rented = True
                print(f"Car has been rented by customer {customer_id}")
                return
        print("Car not available for rental.")

    # function to return a rented car
    def return_car(self, customer_id, make, model):
        for car in self.car_inventory:
            if car.make == make and car.model == model and car.rented:
                car.rented = False
                print(f"Car has been returned by {customer_id}")
                return
        print("Car cannot be returned")

    # HOMEWORK
    # display all the available cars for rent
    # display all the rented cars

    def display_customers(self):
        print("Customer Information:")
        if self.customer_inventory:
            for customer in self.customer_inventory:
                print(customer.get_customer_details())
        else:
            print("No customers in the rental system")

# CREATE A MAIN TO TEST THIS
# e.g. (this was for the carshowroom)
# car1 = Car("Toyota", "Camry", 2022, 25000)
# car2 = Car("Honda", "Civic", 2019, 19000)

# car_showroom = CarShowroom()
# car_showroom.add_car(car1)
# car_showroom.add_car(car2)
# car_showroom.print_all_cars()
# car_showroom.search_car("Honda", "Civic")
# car_showroom.remove_car(car1)
# car_showroom.search_car("Toyota", "Camry")
# car_showroom.print_all_cars()

