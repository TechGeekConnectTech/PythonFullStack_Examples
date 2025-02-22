import moduleos
import csv


#Open file into write mode
server=open("server.txt","w")
server.write("190.12.13.2")
server.write("\n")

#Open file into append mode
server=open("server.txt","a")
server.write("190.12.13.2")
server.write("\n")

#Open file into read mode
server=open("server.txt")
print(server.read())


#Readline()
if os.path.isfile("server.txt"):
    file_read=open("server.txt","r")
    print(file_read.readline())

#Readlines
print("---------------------------------")
if os.path.isfile("server.txt"):
    file_read=open("server.txt","r")
    print(file_read.readlines())

file_read=open("server.txt","r")
for line in file_read:
    print(line)


file_read=open("server.txt","a")
file_read.write("142.13.24.3")
file_read.write("\n")

list=["121.1.1.1\n","121.1.1.1\n","121.1.1.1\n","232.1.1.1\n","111.1.1.1\n","241.1.1.1\n","192.16.1.2\n","198.1.1.1\n"]
file_write=open("server.txt","a")
file_write.writelines(list)

file_write=open("server.txt","a")
for server_list in list:
    file_write.write(server_list)

file_write.close()


os.mkdir("Server")
os.remove("server.txt")
os.rmdir("Server")

print(os.path.exists("server.txt"))
print(os.path.isfile("server.txt"))


list=[]
with open("C:/Users/Mahesh Gavandar/Downloads/student-dataset.csv") as read_file:
    with open("C:/Users/Mahesh Gavandar/Downloads/china.csv","a") as write_file:
        csvfile=csv.reader(read_file)
        for line in csvfile:
            if line[2] == "China":
                list.append(line)

for chine_people in list:
    print(chine_people)
