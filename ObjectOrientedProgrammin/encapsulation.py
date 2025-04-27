class Bank:
    def __init__(self,account_number,account_name,account_branch):
        self._account_number=account_number  #protected
        self.__account_name=account_name     #private
        self.account_branch=account_branch

    def get_account_number(self):
        return self._account_number

    def get_account_name(self):
        return self.__account_name

    def get_account_branch(self):
        return self.account_branch

class Branch(Bank):
    def __init__(self,account_number,account_name,account_branch,branch_address):
        Bank.__init__(self,account_number,account_name,account_branch)
        self.branch_address=branch_address

    def get_branch_address(self):
        return self.branch_address

    def show_all_details(self):
        return self._account_number,self.account_branch,self.branch_address,self.get_account_name()


branch=Branch("0000001","Ranjiv","Sambhajinagar","BaifRoad Pune")
print(branch._account_number)
#print(branch.get_account_name())
#print(branch.account_branch)
#print(branch.branch_address)

print(branch.show_all_details())
