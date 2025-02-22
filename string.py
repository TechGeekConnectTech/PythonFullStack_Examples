name="Ajay"
print(name)

description="""
This is my python class
I am going to learn python
"""
print(description)

#length
print(len(description))
print(len(name))

#Check if string is present
if "python" in description:
    print("Present")

#Check if string is present
if "java" not in description:
    print("Not Present")

#case
name="PUNE"
lowerString=name.lower()
print(name.lower())
print(lowerString)


name="pune mumbai"
UpperString=name.upper()
print(name.upper())
print(UpperString)

name=" pun "
print(name)
str=name.strip()
print(str)


#replace

print(description.replace("python","java"))


print(description[:10])


name="Ajay"
surname="Patil"

print(name + " ### " + surname)