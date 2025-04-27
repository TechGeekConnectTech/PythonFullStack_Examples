from Method_Overriding import test_drive
from devops_operator import names

text="this is python based program"
number=" "

print("Check is Lower :",text.islower())
print("Check the string is digit : ",text.isdigit())
print("Check the string is digit : ",number.isdigit())
print("Check string is numeric :",number.isnumeric())
print("Check string is Alpha :", text.isalpha())
print("Check string is Alphnumeric :", text.isalnum())
print("Check if space is there ?", number.isspace())

'''
name=input("Enter your name ?")
if name.isspace():
    print("Enter Valid name")
else:
    print("This name has been entered :", name)
'''

print("Check number of times string present :",text.count("python"))

if text.islower():
    print("This is lower case text")
else:
    print("It contains upper case character")

print(text.capitalize())

print(text.find("python"))

print(text.upper())
print(text.lower())

print(text.replace("python","java"))
print(len(text))

print(text.split(" "))

