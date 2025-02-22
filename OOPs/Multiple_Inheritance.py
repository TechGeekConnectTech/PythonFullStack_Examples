class University:
    def __init__(self,name,address):
        self.name=name
        self.address=address

    def show_details(self):
        return f"Name is : {self.name} and Address is : {self.address}"

class City:
    def __init__(self,city_name):
        self.city_name=city_name

    def show_city_details(self):
        return f"City is : {self.city_name}"


class College(University,City):
    def __init__(self,name,address,city_name,department_name):
        University.__init__(self,name,address)
        City.__init__(self, city_name)
        self.department_name=department_name

    def show_college_detail(self):
        return f"{self.show_details()},  {self.show_city_details()} and Department is : {self.department_name}"

'''
uni=University("Moze","Wagholi")
print(uni.show_details())
'''

col=College("JSPM","Wagholi","Pune","Computer")
print(col.show_college_detail())

'''
city=City("Pune")
print(city.show_city_details())
'''