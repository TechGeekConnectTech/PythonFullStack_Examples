'''
#for loop syntax
for iterator in <range>
    statement
'''
from random import random

from Operator.operator import students

fruit= {"Banana","Apple","Orange","Papaya","Mango"}

for f in fruit:
    if f in ["Banana","Apple"]:
        print("This is Winter season fruit", f)
    elif f in ["Mango","Papaya"]:
        print("This is Summer season fruit", f)
    elif f in ["Orange"]:
        print("This is Rainy season fruit", f)


for i in range(10):
    if i == 5:
        continue
    print(i)

student=["Subir","Avishek","Gitanjali","Ranjiv","Ayush"]
for s in student:
    if s == "Gitanjali":
        print("Performing some action")
        break

'''
1. create a list of numbers
2. check number is odd or even and seperate into two list

number=[1,10,21,20,30,23,45,68,70,101]

output

odd=[1,21,23,45,101]
even=[10,20,30,68,70]
'''