'''
# Create List
fruit = ["Apple","Orange","Papaya"]
print(fruit)

#duplicate
fruit = ["Apple","Orange","Papaya","Apple"]
print(fruit)

#Index Value Positive
print(fruit[1])

#Index Value Negative
print(fruit[-2])

#Slicing - it'' print 1st and 2nd values
print(fruit[1:3])

#chekc if any item is present

if "Apple" in fruit:
    print("Apple is present in fruit list")

#chekc if any item is not present

if "Mango" not in fruit:
    print("Mango is not present in fruit list")

#List traverse
for item  in fruit:
    print(f"{item} is present in fruit list")

# Update list
fruit[3]="Mango"

#Add value
fruit.append("Kiwi")
print(fruit)


#Append list
student1=["Ajay","Ranjiv","Mahesh"]
student2=["Sakshi","Dhanshree","Priya"]
student1.append(student2)
print(student1)

# Merge list
student1=["Ajay","Ranjiv","Mahesh"]
student2=["Sakshi","Dhanshree","Priya"]
for item in student2:
    student1.append(item)

print(student1)

#add list
student1=["Ajay","Ranjiv","Mahesh"]
student2=["Sakshi","Dhanshree","Priya"]
student1=student1+student2
print(student1)
'''
#exdend
student3=[]
student1=["Ajay","Ranjiv","Mahesh"]
student2=["Sakshi","Dhanshree","Priya"]
student3=student1.extend(student2)
print(student1)

#delete elements

student1=["Ajay","Ranjiv","Mahesh"]
student1.pop(1)
print(student1)

#delete list

student1=["Ajay","Ranjiv","Mahesh"]
del student1

#clear and length of list
student1=["Ajay","Ranjiv","Mahesh"]

print(len(student1))
student1.clear()
print(student1)

student=["Ajay","Ranjiv","Mahesh"]
item1=[name for name in student if name=="Ranjiv"]
print(item1)

item1=[]
student=["Ajay","Ranjiv","Mahesh"]
for name in student:
    if name is "Ranjiv":
        item1.append("Ranjiv")
print(item1)