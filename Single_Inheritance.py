class Car: # Base Class
    def __init__(self,brand,model,year):
        self.brand=brand
        self.model=model
        self.year=year

    def display_info(self):
        return f"Car information is Brand : {self.brand},Model : {self.model},Year : {self.year}"


class Electric_Car(Car): # Derived Class
    def __init__(self,brand,model,year,battery_capacity):
        super().__init__(brand,model,year) #Inherit Properties and Method using super()
        self.battery_capacity=battery_capacity

    def display_battery_information(self):
        return f"Battery Capacity {self.battery_capacity} KWH"

car=Car("Toyota","Camry",2024)
print(car.display_info())


ecar=Electric_Car("Tesla","Model S",2024,100)
print(ecar.display_info())
print(ecar.display_battery_information())