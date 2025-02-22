list=[]
with open("server.txt") as file:
    for line in file:
        list.append(line.split(" "))

value=[]
for num in list:
    value.append(num[2])

print(value)

list1=[]
with open("server1.txt") as file:
    for line in file:
        list1.append(line.split(" "))

value1=[]
for num in list1:
    value1.append(num[2])

print(value1)

master=[]
master.append(value)
master.append(value1)
print(master)