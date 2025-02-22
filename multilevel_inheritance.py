class Vehicle:
    def __init__(self,brand,wheels):
        self.brand=brand
        self.wheels=wheels

class Car(Vehicle):
    def __init__(self,brand,wheels,model,fuel_type):
        Vehicle.__init__(self,brand,wheels)
        self.model=model
        self.fuel_type=fuel_type

    def show_car_details(self):
        return f"Car Brand : {self.brand}, Wheels : {self.wheels}, Model : {self.model}, Fuel Type : {self.fuel_type}"

class ElectricCar(Car):
    def __init__(self,brand,wheels,model,fuel_type,battery_type):
        Car.__init__(self,brand,wheels,model,fuel_type)
        self.battery_type=battery_type

    def show_all_car_details(self):
        return f"Car Detail : {self.show_car_details()}, Battery Detail : {self.battery_type}"

car=ElectricCar("Toyota","4 Wheels","SUV","Diesel","100")
print(car.show_all_car_details())


