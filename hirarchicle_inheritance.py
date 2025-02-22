# Base class
class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}")


# Derived class 1
class Car(Vehicle):
    def __init__(self, make, model, doors):
        super().__init__(make, model)  # Call the base class constructor
        self.doors = doors

    def display_car_info(self):
        self.display_info()  # Call the method from the base class
        print(f"Doors: {self.doors}")


# Derived class 2
class Truck(Vehicle):
    def __init__(self, make, model, capacity):
        super().__init__(make, model)  # Call the base class constructor
        self.capacity = capacity

    def display_truck_info(self):
        self.display_info()  # Call the method from the base class
        print(f"Capacity: {self.capacity} tons")


# Creating objects of Car and Truck
car = Car("Toyota", "Camry", 4)
truck = Truck("Ford", "F-150", 2)

# Displaying info
car.display_car_info()
print()
truck.display_truck_info()