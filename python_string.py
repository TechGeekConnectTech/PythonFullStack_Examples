from string import surname
from variable import city_name

name="Ajay 1"
feedback='''
TechGeekConnect is one best training institute in Pune.
All Trainers are working in IT Industries, so its a good place to upskill
'''
print(name)
print(feedback)

#Lenth Check
print(len(name))
print(len(feedback))

#check if present
if "Pune" in feedback:
    print("Pune is present in feeback")

#check if not present
if "Mumbai" not in feedback:
    print("Mumbai is not present in feeback")

print("----------------------------------------------------------")
print(feedback[8:32])
print(feedback[32:])
print(feedback[:8])

print("----------------------------------------------------------")

#Upper case
city_name="pune"
print(city_name.upper())

#Lower case
city_name="PUNE doijwqiodjSWDWDDM WDMKLW WLKkwmdkmlkwdqwd DWDNKlknlkeqcece"
print(city_name.lower())

#Strip
city_name=" pune "
print(city_name)
print(city_name.strip())

#Replace
print(feedback.replace("Pune","Chh.Smbhajinagar"))

name="Ajay"
Surname="Patil"

print(name + " - " +Surname)

fullname=name+surname
print(fullname)

print(f"My Name is : {fullname}")