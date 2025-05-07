# Assignment 1: Create Your Own Class - Smartphone

class Smartphone:
    # Constructor to initialize attributes
    def __init__(self, brand, model, battery):
        self.brand = brand
        self.model = model
        self.battery = battery

    # Method to charge the phone
    def charge_phone(self):
        self.battery = 100
        print(f"{self.brand} {self.model} is now fully charged!")

    # Method to simulate using an app
    def use_app(self, app_name):
        if self.battery > 10:
            self.battery -= 10
            print(f"Using {app_name}... Battery level is {self.battery}%.")
        else:
            print("Battery is too low. Please charge your phone.")

    # Method to display phone details
    def display_phone_info(self):
        print(f"Brand: {self.brand}\nModel: {self.model}\nBattery: {self.battery}%")


# Activity 2: Polymorphism Challenge with Vehicles

class Vehicle:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method.")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


# Function to demonstrate polymorphism
def perform_move_action(vehicle):
    vehicle.move()

# Testing Smartphone class
print("---- Smartphone Test ----")
my_phone = Smartphone("Samsung", "Galaxy S23", 50)
my_phone.display_phone_info()
my_phone.use_app("YouTube")
my_phone.charge_phone()

# Testing Polymorphism with vehicles
print("\n---- Vehicle Test ----")
my_car = Car()
my_plane = Plane()

perform_move_action(my_car)   # Output: Driving 🚗
perform_move_action(my_plane)  # Output: Flying ✈️
