class Honda:
    def __init__(self,company_name,company_address):
        self.company_name=company_name
        self.company_address=company_address

    def show_company_details(self):
        return self.company_name,self.company_address

class HondaCar(Honda):
    def __init__(self,company_name,company_address,car_name):
        super().__init__(company_name,company_address)
        self.car_name=car_name


class HondaBike():
    def __init__(self, bike_name):
        #super().__init__(company_name, company_address)
        self.bike_name=bike_name


class HondaCustomer(HondaCar,HondaBike):
    def __init__(self,company_name,company_address,car_name,bike_name,customer_name):
        HondaCar.__init__(self,company_name,company_address,car_name)
        HondaBike.__init__(self,bike_name)
        self.customer_name=customer_name

    def show_all_details(self):
        return self.company_name,self.company_address,self.car_name,self.bike_name,self.customer_name


hc=HondaCustomer("Honda","Japanese","City Honda","CBZ","Ranjiv")
print(hc.show_all_details())


