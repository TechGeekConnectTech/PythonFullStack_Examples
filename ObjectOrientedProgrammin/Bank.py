class Bank:
    def __init__(self):
        self.branch_code = None
        self.branch_name = None
        self.branch_address = None
    '''
    def __init__(self,branch_code,branch_name, branch_address):
        self.branch_code=branch_code
        self.branch_name=branch_name
        self.branch_address=branch_address
    '''
    def set_bank_information(self,branch_code,branch_name,branch_address):
        self.branch_code = branch_code
        self.branch_name = branch_name
        self.branch_address = branch_address

    def get_bank_information(self):
        return self.branch_code,self.branch_name,self.branch_address


def get_bank_information():
    return get_bank_information()

#sbi=Bank("SBIN1234","SBI FC Road","Sivaji Nagar, Pune")
sbi=Bank()
sbi.set_bank_information("SBIN1234","SBI FC Road","Sivaji Nagar, Pune")
#sbi.__init__("SBIN1234","SBI FC Road","Sivaji Nagar, Pune")
print(sbi.get_bank_information())
print("Branch Name : ",sbi.branch_name)


