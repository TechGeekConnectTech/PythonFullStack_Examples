#while <condition>:
#    Action
import random

from sample import student

i=1
'''
while i <= 10:
    print(i)
    i=i+1
'''

for i in range(10):
    print(i)

students = ["Pradeep","Mahesh","Rashmi","Dhanshree","Sakshi","Ajinath"]

for name in students:
    if name is "Sakshi":
        break
    else:
        print(name)

for name in students:
    if name is "Mahesh":
        continue
    else:
        print(f"{name}:  all are the DevOps Batch Students")


dict1 = {
    "name":"Pradeep",
    "roll":1,
    "city":"Pune"
}
dict2 = {
    "name":"Ajinath",
    "roll":2,
    "city":"Aurangabad"
}
students=[]
students.append(dict1)
students.append(dict2)

for student in students:
    if student["city"] == "Aurangabad":
        student["city"]="Chh. Sambhajinagar"

print(students)

