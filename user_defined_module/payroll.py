class Payroll:
    @staticmethod
    def show_salary(empid):
        # Check this employee id is present in Database
        # Fetch Employee salary structure from Database
        # Covert into Json
        salary = {
            "empid": "00012",
            "employee_name":"Ayush Lakde",
            "employee_address": "Mumbai",
            "Basic Salary": "67000",
            "Allowance": "120000",
        }
        return salary

    @staticmethod
    def insert_salary(empid,basic_salary,allowance):
        # Check this employee id is present in Database
        # Fetch Employee Record from Database
        #insert salary into Database
        salary = {
            "empid": empid,
            "employee_name":"Ayush Lakde",
            "employee_address": "Mumbai",
            "Basic Salary": basic_salary,
            "Allowance": allowance,
        }
        success ={
            "return_code":200,
            "message": "Employee Data inserted Successfully"
        }
        return success
