# Base class
class Car:
    def start_engine(self):
        print("Starting the car's engine...")

    def drive(self):
        print("The car is driving on the road.")

# Derived class 1
class ElectricCar(Car):
    def start_engine(self):
        print("Starting the electric car silently...")

    def drive(self):
        print("The electric car is driving with zero emissions.")

# Derived class 2
class SportsCar(Car):
    def start_engine(self):
        print("Starting the sports car with a roar!")

    def drive(self):
        print("The sports car is zooming on the highway.")

# Function demonstrating runtime polymorphism
def test_drive(car):
    car.start_engine()
    car.drive()

# Creating objects
generic_car = Car()
tesla = ElectricCar()
ferrari = SportsCar()

# Demonstrating runtime polymorphism
print("Generic Car:")
test_drive(generic_car)
print("\nElectric Car:")
test_drive(tesla)
print("\nSports Car:")
test_drive(ferrari)
