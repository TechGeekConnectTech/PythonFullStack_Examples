class student:
    def __init__(self,name,surname):
        self.name = name
        self.surname = surname

    def marks(self,m1,m2,m3):
        return m1+m2+m3

s1=student("Mahesh","Gavandar")
print(s1.name)
print(s1.surname)
s1.name="Ajit"
print(s1.name)
marks=s1.marks(10,20,30)
print(marks)