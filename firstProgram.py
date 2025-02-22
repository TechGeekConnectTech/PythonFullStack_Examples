'''
name = "Ajay"
number = 1
student_list = ["Ajay","Ajinath","Ranjiv"]
student_tuple = ("Ajay","Ajinath","Ranjiv")
student_dict = {"name":"Ajay","roll":1,"address":"Pune"}

print(type(name))
print(type(number))
print(type(student_list))
print(type(student_tuple))
print(type(student_dict))

print(name)
print(number)
print(student_list)
print(student_tuple)
print(student_dict)

#case sensative

name="Ajay"
Name="Ajinath"
NAME="Ranjiv"

print(name)
print(Name)
print(NAME)


name="Ajay"
name="Ajinath"
name="Ranjiv"

print(name)
print(name)
print(name)

#Varible Names
city_name="Pune" # good practice - snake case
cityName="Mumbai" #good practice - camel case
CityName="Delhi" #good practice - pascal case

x="Pune"  # Not a good practice


fruit1="Apple"
fruit2="Mango"
fruit3="banana"

print(fruit1)
print(fruit2)
print(fruit3)

fruit1,fruit2,fruit3="Apple","Mango","banana"

print(fruit1)
print(fruit2)
print(fruit3)

fruit1=fruit2=fruit3="Apple","Mango","Banana"

print(fruit1)
print(fruit2)
print(fruit3)

fruit=["Apple","Banana","Mango","Orange"]
a,b,c,d=fruit
print(a)
print(b)
print(c)
print(d)


a,b,c,d=["Apple","Banana","Mango","Orange"]

print(a)
print(b)
print(c)
print(d)

'''
#Example 1
def my_func():
   global name
   name = "Ajinath"


my_func()
print(name)

#Example 2

def my_func():
   name = "Ajinath"
   return name

a=my_func()
print(a)