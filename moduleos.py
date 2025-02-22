import moduleos
print(os.getcwd())
print(os.listdir())
print(os.listdir('C:/Users/Mahesh Gavandar/Documents'))
os.chdir('C:/Users/Mahesh Gavandar/Documents')
print(os.listdir())
print(os.getcwd())
os.mkdir('Test')
os.rmdir('Test')

print(os.path.exists('C:/Users/Mahesh Gavandar/Documents'))
print(os.path.isfile('C:/Users/Mahesh Gavandar/Documents/Resume.txt'))
print(os.path.isdir('C:/Users/Mahesh Gavandar/Documents'))

print(os.environ)
print(os.environ.get("ONEDRIVECONSUMER"))
os.environ["ANSIBLE"]="Power"
print(os.environ.get("ANSIBLE"))

os.system("dir")

print(os.getpid())
print(os.getlogin())