from ObjectOrientedProgrammin import Bank
sbi=Bank()
sbi.set_bank_information("SBIN1234","SBI FC Road","Sivaji Nagar, Pune")
#sbi.__init__("SBIN1234","SBI FC Road","Sivaji Nagar, Pune")
print(sbi.get_bank_information())
print("Branch Name : ",sbi.branch_name)
