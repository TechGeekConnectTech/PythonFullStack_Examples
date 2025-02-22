class Car:
   def show_details(self,*args):
       if len(args) == 1:
           print(f"One Argumnet Passed : {args[0]}")

       elif len(args) == 2:
           print(f"Two Argumnet Passed : {args[0]} and {args[1]}")

       elif len(args) == 3:
           print(f"Three Argumnet Passed : {args[0]} and {args[1]} and {args[2]}")


car=Car()
car.show_details("Hyundai")
car.show_details("Hyundai","Maruti")
car.show_details("Hyundai","Maruti","Honda")