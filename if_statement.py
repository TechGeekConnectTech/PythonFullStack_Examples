students = ("Pradeep","Mahesh","Rashmi","Dhanshree","Sakshi","Ajinath")

if "Rashmi" in students:
    print("Rashmi is part of list")

number1=20
number2=20
if number1 < number2:  #if condition is True -> inside block
    print("Number1 is less than number2 ")
elif number1 > number2:
    print("Number1 is greater than number2 ")
else:
    print("Number1 is equal to  number2 ")


if number1 is number2:
    print("Both number are same")

students = ["Pradeep","Mahesh","Rashmi","Dhanshree","Sakshi","Ajinath"]

if "Pradeep" in students:
    if "Mahesh" in students:
        if "Rashmi" in students:
            print("All three conditions are met")


if students:
    if "Pradeep" in students:
        print("Pradeep is in Students list")

