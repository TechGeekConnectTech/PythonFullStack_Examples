from devops_list import fruit
from dictionary import student1

student = {
    "name":"Ajay",
    "Rollnumber":1,
    "City":"Mumbai"
}

print(student)

#get Keys
print(student.keys())

#get values
print(student.values())

student.clear()
print(student)

student = {
    "name":"Ajay",
    "Rollnumber":1,
    "City":"Mumbai"
}

student["name"]="Sakshi"

print(student)

print(student["City"])