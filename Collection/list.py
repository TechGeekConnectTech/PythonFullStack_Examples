'''
string_list=["Subir","Gitanjali","Avishek","Subir"]
print(string_list)
print(string_list[1])
string_list[1]="Ranjiv"
print(string_list)
#check lenght of list
print(len(string_list))
print(type(string_list))

surname=["shah","varma","sharma"]
concati=string_list+surname
print(concati)

a=string_list.append(surname)
print(string_list)
print(string_list[3])
print(string_list[4][2])
print(string_list[1:4])

if "Avishek" in string_list:
    print("Yes")
else:
    print("Not Present")

if "shah" in string_list[4]:
    print("Yes")
else:
    print("Not Present")
'''

fruit=["Banana","Apple","Cherry","Papaya","Banana"]
print("Banana Occurance ",fruit.count("Banana"))
fruit.remove("Banana")
fruit.remove("Banana")
print("Remove Banana from list",fruit)
fruit.pop(1)
print("pop 1st element from list",fruit)
fruit.clear()
print("Clear list",fruit)
fruit=["Banana","Apple","Cherry","Papaya","Banana"]
fruit.reverse()
print("Reverse List :",fruit)
fruit.sort()
print("Sorting",fruit)

for f in fruit:
    if f == "Apple":
        print(f)

fruit.insert(1,"Watermelon")
print(fruit)