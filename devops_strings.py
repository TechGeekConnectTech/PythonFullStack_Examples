name="my name is Ajinath"
print(name.capitalize())
number="12345678"
if number.isdigit():
    print("This is valid number")

name="Pradeep"
if name.islower():
    print("This is lower case")

names="Ajinath Pradeep Rashimi Sakshi Dhanshree"
print(names.split(" ")[1])

new_names=names.replace("Pradeep","Mahesh")
print(new_names)

print(len(names))