import json

customer={
    "CustId":"C0001",
    "CustomerName":"Ajay Pandey",
    "CustomerAddress":"Mumbai",
    "CustomerPhone":987654321
}

print(type(customer))
print("Customer Dict :",customer)

#Dumps - is use for to convert Dictionary to String
json_string=json.dumps(customer)
print(type(json_string))
print("Customer Json :",json_string)
#print("Print Customer Name :",json_string['CustomerName'])

#dump json_string to file
with open("customer.json","w") as file_ptr:
    json.dump(json_string,file_ptr)

with open("customer.json","w") as file_ptr:
    json.dump(json_string,file_ptr)

#load is use for loading json file into json string

with open("customer.json","r") as file_name:
    data=json.load(file_name)
print("Type of Data:",print(type(data)))
print("Show Data : ",data)

#Loads - is use for to convert Json String to Dictionary
convert_dict=json.loads(json_string)
print(type(convert_dict))
print("Print Customer Name :",convert_dict["CustomerName"])



