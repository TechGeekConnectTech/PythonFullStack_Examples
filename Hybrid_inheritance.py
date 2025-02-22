# Base class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"Vehicle: {self.brand} {self.model}")

# Derived class 1 (inherits from Vehicle)
class Car(Vehicle):
    def __init__(self, brand, model, doors):
        super().__init__(brand, model)
        self.doors = doors

    def car_details(self):
        print(f"Car: {self.brand} {self.model}, Doors: {self.doors}")

# Derived class 2 (inherits from Vehicle)
class ElectricVehicle(Vehicle):
    def __init__(self, brand, model, battery_capacity):
        super().__init__(brand, model)
        self.battery_capacity = battery_capacity

    def ev_details(self):
        print(f"Electric Vehicle: {self.brand} {self.model}, Battery: {self.battery_capacity} kWh")

# Derived class 3 (inherits from Car and ElectricVehicle)
class HybridCar(Car, ElectricVehicle):
    def __init__(self, brand, model, doors, battery_capacity, fuel_efficiency):
        Car.__init__(self, brand, model, doors)
        ElectricVehicle.__init__(self, brand, model, battery_capacity)
        self.fuel_efficiency = fuel_efficiency

    def hybrid_details(self):
        print(f"Hybrid Car: {self.brand} {self.model}, Doors: {self.doors}, "
              f"Battery: {self.battery_capacity} kWh, Fuel Efficiency: {self.fuel_efficiency} km/l")

# Demonstrating the hybrid inheritance
hybrid_car = HybridCar("Toyota", "Prius", 4, 8.8, 25)
hybrid_car.show_details()  # From Vehicle
hybrid_car.car_details()   # From Car
hybrid_car.ev_details()    # From ElectricVehicle
hybrid_car.hybrid_details()  # From HybridCar
