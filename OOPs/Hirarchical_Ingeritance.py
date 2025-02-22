class City:
    def __init__(self,city_name):
        self.city_name=city_name

    def show_city_details(self):
        return f"City is : {self.city_name}"


class University(City):
    def __init__(self,city_name,name,address):
        City.__init__(self,city_name)
        self.name=name
        self.address=address

    def show_details(self):
        return f"Name is : {self.name} and Address is : {self.address}, {self.show_city_details()}"



class College(City):
    def __init__(self,city_name,college_name,department_name):
        City.__init__(self, city_name)
        self.college_name=college_name
        self.department_name=department_name

    def show_college_detail(self):
        return f"{self.show_city_details()} and College is : {self.college_name},Department is : {self.department_name}"



'''
uni=University("Moze","Wagholi")
print(uni.show_details())
'''
'''
col=College("JSPM","Wagholi","Pune","Computer")
print(col.show_college_detail())
'''
'''
city=City("Pune")
print(city.show_city_details())
'''


uni=University("Pune","SavitriBai","ShivajiNagar")
print(uni.show_details())

col=College("Pune","Moze","Computer")
print(col.show_college_detail())