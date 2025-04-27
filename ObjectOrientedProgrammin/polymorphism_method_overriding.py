class Car:
    def show_details(self,*args):
        if (len(args) == 1):
            print("One Arguments has been passed")
        elif (len(args) == 2):
            print("Two Arguments has been passed")
        elif (len(args) == 3):
            print("Three Arguments has been passed")

car=Car()
car.show_details("Hyundai")
car.show_details("Hyundai","Maruti")
car.show_details("Hyundai","Maruti","Wolkwagon")