class Bank:
    def __init__(self,bank_name,bank_headquarter):
        self.bank_name=bank_name
        self.bank_headquarter=bank_headquarter

    def show_bank(self):
        return self.bank_name,self.bank_headquarter

class SBIBank(Bank):
    def __init__(self,bank_name,bank_headquarter,branch_code,branch_name,branch_address):
        super().__init__(bank_name,bank_headquarter)
        self.branch_code=branch_code
        self.branch_name=branch_name
        self.branch_address=branch_address

    def branch_info(self):
        return self.branch_code,self.branch_name,self.branch_address

    def update_branch_code(self,branch_code):
        self.branch_code=branch_code


class Branch(SBIBank):
    def __init__(self,bank_name,bank_headquarter,branch_code,branch_name,branch_address,account_no, account_name, account_address):
        super().__init__(bank_name,bank_headquarter,branch_code,branch_name,branch_address)
        self.account_no=account_no
        self.account_name=account_name
        self.account_address=account_address

    def show_customer_info(self):
        return self.branch_code,self.branch_name,self.branch_address,self.account_no, self.account_name, self.account_address



vbranch=Branch("SBIN","Mumbai","SBIN1234","SBIN Viman Nagar","Viman Nagar,Pune","XYZ","Ayush","Aurangabad")
print(vbranch.show_bank())
sbranch=Branch("AXIS","Pune","AXISNXYZ","AXIS Nariman Point","Mumbai","ABC","Vijay Mallya","London")
print(sbranch.show_bank())
'''
print(vbranch.branch_info())
print(vbranch.show_customer_info())
print(sbranch.branch_info())
print(sbranch.show_customer_info())


bank=SBIBank("SBIN1234","SBIN Viman Nagar","Viman Nagar,Pune")
bank.update_branch_code("SBINXYZ")
bc,bn,ba=bank.branch_info()

print("Branch Code is : ",bc)
print("Branch Name is :", bn)
print("Branch Address is :",ba)
'''