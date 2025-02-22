from list import student

fruit = ["Apple","Orange","Banana"]

print(fruit)

#index
print(fruit[1])

#Adding value to the list
fruit.append("Mango")

#Update list
fruit[1]="Papaya"
print(fruit)

#delete element
fruit.pop(1)

print(fruit)

del fruit

fruit = ["Apple","Orange","Banana"]
fruit.pop(0)
fruit.pop(1)
print(fruit)

fruit.clear()
print(fruit)

fruit1 = ["Apple","Orange","Banana"]
fruit2 = ["Mango","Papaya","Kiwi"]

fruit1.extend(fruit2)
print(fruit1)

fruit3=fruit1+fruit2
print(fruit3)

print(len(fruit3))

Students = ["Ajinath","Akshy","Prakash","Aarti"]
if "Pradeep" not in Students:
    print("Pradeep is not part of Students")

for name in Students:
    print(name)

Students.remove("Aarti")
print(Students)