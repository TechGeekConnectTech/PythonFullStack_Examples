

description="""
This is my python class
we are learning variables
Python is most popular language
"""

#int
number=1
print(number)
print(type(number))

#string
name="Ajay"
print(name)
print(type(name))

#float
percentage=80.12
print(percentage)
print(type(percentage))


#multi line string
print(description)
print(type(description))

#list
student_list = ["Ajay","Ajinath","Pradeep","Sakshi","Dhanshree"]
print(student_list)
print(type(student_list))

#tuple
student_tuple = ("Ajay","Ajinath","Pradeep","Sakshi","Dhanshree")
print(student_tuple)
print(type(student_tuple))

#dictionary
student_dict={"name":"Pradeep","roll_number":2,"city":"Pune"}
print(student_dict)
print(type(student_dict))

#None
name=None
print(name)
print(type(name))

#casting
roll_number=int("1")
print(roll_number)
print(type(roll_number))

#case sensative
name="Ajay"
Name="Ajinath"
NAME="Pradeep"
print(name)
print(Name)
print(NAME)

#Best practice variable names
cityName="Pune" #camel case
CityName="Mumbai" #pascal case
city_name="Delhi" #snake cass
_cityName="Punjab" #

number1=1



name1,name2,name3="sakshi","Pradeep","Rashmi"
print(name1)
print(name2)
print(name3)

name1=name2=name3="Sakshi"
print(name1)
print(name2)
print(name3)


# Global Variable

def addition(number1,number2):
    global add
    add=number1+number2

addition(2,3)
print(add)

def addition(number1,number2):
    add=number1+number2
    return add

sum=addition(2,3)
print(sum)
