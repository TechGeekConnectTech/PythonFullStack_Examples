class Car:
    def show_details(self,*args):
        if len(args) == 1:
            print(f"Argument 1 Passed : {args[0]}")
        elif len(args) == 2:
            print(f"Argument 2 Passed : {args[0]} and {args[1]}")

car=Car()
car.show_details("Sandeep")
car.show_details("Sandeep","Sonne")