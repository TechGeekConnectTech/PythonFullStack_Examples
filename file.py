import csv
'''
file_object = open("student.txt","a")
file_object.write("My Name is Rashmi")
file_object.write("\n")

file_object = open("student.txt","r")
print(file_object.read())

file_object = open("student.txt","r")
#print(file_object.readline())
print(file_object.readlines())

for line in file_object:
    if "Mahesh" in line:
        print("found")

file_object = open("C:/Users/Mahesh Gavandar/Downloads/student-dataset.csv","r")
list=[]
for line in file_object:
    list.append(line)


with open("C:/Users/Mahesh Gavandar/Downloads/student-dataset.csv","r") as file_read:
    with open("C:/Users/Mahesh Gavandar/Downloads/student-dataset1.csv", "a") as file_write:
        file_write.writelines(file_read.readlines())
'''
list=[]
with open("C:/Users/Mahesh Gavandar/Downloads/student-dataset.csv","r") as file_read:
    csvFile=csv.reader(file_read)

    for line in csvFile:
       list.append(line)

for line in list:
    if line[2] == "China":
        print(line)
