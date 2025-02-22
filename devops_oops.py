class student:
    #Constructor Function - Default Constructor
    def __init__(self):
        self.name="Ajinath"
        self.surname="Patil"

    def show(self):
        print(f"My Name is : {self.name} and Surname is {self.surname}")

class Teacher:
    #Constructor Function - Parameterized Constructor
    def __init__(self,name,surname):
        self.name=name
        self.surname=surname

    def show(self):
        print(f"My Name is : {self.name} and Surname is {self.surname}")


s1=student()
s1.show()
del s1.name

del s1

t1=Teacher("Pradeep","Khandagle")
t1.show()