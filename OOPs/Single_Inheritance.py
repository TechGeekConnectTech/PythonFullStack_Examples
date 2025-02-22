class University:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def show_details(self):
        return f"Name is : {self.name} and Address is : {self.address}"

class College(University):
    def __init__(self,name,address,department_name):
        University.__init__(self,name,address)
        self.department_name=department_name

    def show_college_detail(self):
        return f"{self.show_details()} and Department is : {self.department_name}"

uni=University("Moze","Wagholi")
print(uni.show_details())

col=College("JSPM","Pune","Computer")
print(col.show_college_detail())