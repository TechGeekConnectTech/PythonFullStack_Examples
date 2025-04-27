import os
import datetime
print("Get Current Working Directory",os.getcwd())
print("Check file is present",os.path.isfile("student.txt"))
print("Check Environment Variables ",os.environ)
print("Print Environment Variables :",os.environ['HOMEPATH'])
os.environ["SKILL"]="Python"
print("Print Environment Variables :",os.environ['SKILL'])
print("Get Computer Name",os.name)
print("Get Process Id",os.getpid())
curret_worl=os.getcwd()
log_file="log.txt"
file_path=os.path.join(curret_worl,log_file)
date=datetime.datetime.now()
with open(file_path,"w") as file_write:
    file_write.write(f"{date},Writing Logs into file")


#print(os.remove("student.txt"))