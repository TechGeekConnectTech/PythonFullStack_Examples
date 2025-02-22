import csv

import moduleos

#Write FIle
file_obj=open(s)
'''
file_obj.write("Apple")
file_obj.write("\n")
file_obj.close()

#Append File
file_obj=open("fruit.txt","a")
file_obj.write("Apple")
file_obj.write("\n")
file_obj.close()


#Read FIle
file_obj=open("fruit.txt","r")
print(file_obj.read())
print(file_obj.readline())
print(file_obj.readlines())
for line in file_obj:
    print(line)
file_obj.close()


fruit=["Mango\n","Banana\n","Pineapple\n","Kiwi\n","Papaya\n"]
file_obj=open("fruit.txt","w")
file_obj.writelines(fruit)

fruit=["Mango\n","Banana\n","Pineapple\n","Kiwi\n","Papaya\n"]
file_obj=open("fruit.txt","w")
for list in fruit:
    file_obj.write(list)
file_obj.close()


#os.mkdir("Fruit")
if os.path.exists("pradeep.txt"):
    file_obj=open("fruit.txt","r")
    print(file_obj.read())
else:
    print("Pradeep.txt file is not present")

#os.rmdir("Fruit")
#os.remove("fruit.txt")
'''

with open("D:/student-dataset.csv","r") as file_obj:
    with open("india.csv","w") as file_write:
        csvfile=csv.reader(file_obj)
        for line in csvfile:
            if line[2] == "India":
                file_write.writelines(line)
                file_write.write("\n")
