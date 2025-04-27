from user_defined_module.payroll import Payroll as p
try:
    print(p.show_salary("00012"))
    print(p.insert_salary("00012","10000","12000"))
except Exception as e:
    print("Exception triggered :",e)