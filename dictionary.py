student1={
    "name":"Mahesh",
    "roll":"1",
    "city":"Pune"
}

student2={
    "name":"Ranjiv",
    "roll":"2",
    "city":"Mumbai"
}
student3=[]
student3.append(student1)
student3.append(student2)

for name in student3:
    print(name["name"])