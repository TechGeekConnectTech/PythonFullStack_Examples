#Arithmetic operation
number1=20
number2=8

print(number1+number2)
print(number1-number2)
print(number1*number2)
print(number1/number2)
print(number1%number2)
print(number1**number2)

#Comparision operator
number1=20
number2=20
if number1>number2:
    print("Number1 is greater than number2")

if number1<number2:
    print("Number1 is less than number2")

if number1>=number2:
    print("Number1 is greather than equal to number2")

if number1<=number2:
    print("Number1 is less than equal to number2")


#Logical Operator
names = ["Ajay","Atul","Pradeep","Sakshi"]
if "Dhanshree" not in names and "Rahsmi" not in names:
    print("Dhanshree and Rashmi is not part of names")

#Identity
name1="Ajay"
name2="Ajinath"

if name1 is not name2:
    print("True")
else:
    print("False")