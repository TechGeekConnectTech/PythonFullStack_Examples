import os

print("Current Working Directory:",os.getcwd())
os.chdir('D:/sandbox/PythonPro/Module')
print("Current Working Directory:",os.getcwd())
#print("Create New Directory",os.mkdir("Test"))
#os.chdir('D:/sandbox/PythonPro/Module/Test')
#open("test.txt","w")
print(os.listdir())
#os.remove("test.txt")
print(os.listdir())
os.chdir('D:/sandbox/PythonPro/Module/')
#os.rmdir('Test')
#os.rename("test.txt","car.txt")

print("My Current Process Id:",os.getpid())

print(f"Show all Environment Variables:",os.environ)
print("Specific Environment Variables :",os.environ["USERNAME"])
os.environ["COMPANYNAME"]="TechGeekConnect Technologies"
print(os.environ["COMPANYNAME"])


print(os.path.isdir("D:/sandbox/PythonPro/Module"))
print(os.path.isfile("D:/sandbox/PythonPro/Module/car1.txt"))
print(os.path.exists("D:/sandbox/PythonPro/Module"))

print(os.path.abspath("D:/sandbox/PythonPro/Module"))


print(os.popen("dir").read())

folderpath="D:\sandbox\PythonPro"
folder="Exception Handling"
file_name="college.txt"

filepath=os.path.join(folderpath,folder,file_name)

with open(filepath,"w") as file:
    file.write("Writing logs")