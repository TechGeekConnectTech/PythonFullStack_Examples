class Car:
    def start_engine(self):
        print("Starting Engine of Car")

    def drive(self):
        print("This Car is Driving on Road")


class Electric(Car):
    def start_engine(self):
        print("Start Electric Car Engine")

    def drive(self):
        print("Driving Electric Car")

class SportsCar(Car):
    def start_engine(self):
        print("Start Sports Car Engine")

    def drive(self):
        print("Driving Sports Car")

#Run time polymorphism
def test_runtime(xyz):
    xyz.start_engine()
    xyz.drive()

car=Car()
electric=Electric()
sportscar=SportsCar()

test_runtime(car)
test_runtime(electric)
test_runtime(sportscar)

'''
electric.start_engine()
electric.drive()

sportscar.start_engine()
sportscar.drive()

car.start_engine()
car.drive()
'''