class Student:
    '''
    #default constructor
    def __init__(self):
        self.name=""
        self.surname = ""
        print("Im in Constructor")
    '''

    # Parameterized constructor
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname
        print("Im in Parameterized Constructor")

    def show_name_surname(self):
        return f"My name is {self.name} and Surname is {self.surname}"

    def show_name(self,name,surname):
        self.name=name
        print(f"Student name is {self.name}")
        self.surname = surname
        print(f"Student surname is {self.surname}")


    def show_surname(self, surname):
        self.surname = surname
        print(f"Student surname is {self.surname}")

#s1=Student()
s2=Student("Ranjiv","Gupta")

print(s2.show_name_surname())
del s2.name
del s2
print(s2.show_name_surname())



#s1.show_name("Ranjiv","Gupta")

#s1.show_surname("Gupta")

'''
s1.show("Ranjiv")
s1.show("Mahesh")

s2=Student()

s2.show("Ranjiv")
s2.show("Mahesh")
'''