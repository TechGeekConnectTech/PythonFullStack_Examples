from devops_oops import student

number1=2
number2=23
name="Subir"
surname="shah"

print("Addition of two number :",number1+number2)
print("Substraction of two number :",number1-number2)
print("Multiplication of two number :",number1*number2)
print("Division of two number :",number1/number2)
print("MOdulus of two number :",number1%number2)
print("Exponentials :",number1**number2)
print("My full name is :",name +" "+surname)

if number1 == number2:
    print("Both Number are same")

if number1 != number2:
    print("Both Number are not same")

if number1 > number2:
    print("number1 is greater than number2")


if number1 < number2:
    print("number1 is less than number2")

choice="Delhi"
salary=10
if not (choice=="Mumbai" or choice=="Pune") and salary == 10:
    print("Process for interview")
else:
    print("Rejet the candidates")

name="Subir"

if name == "Subir":
    print("Same")

number=10

if number is 10:
    print("same")


text="this is python based program"
if "python" in text:
    print("String is present")

students=["Subir","Gitanjali","Ayush","Avishek"]
if "Ranjiv" not in students:
    print("Student is not present in list")