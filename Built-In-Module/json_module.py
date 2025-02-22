import json
student=[{
    "name":"Pradeep",
    "Age":24,
    "Address":"Pune",
    "Marks":{
    "Math":90,
    "English":100
    }
},
{
    "name":"Sagar",
    "Age":20,
    "Address":"Mumbai"
}]

#for li in student:
 #   print(li["name"])

    
jsondata1=json.dumps(student,indent=4)
with open("student_data.json","w") as file:
    file.write(jsondata1)


with open("student_data.json","r") as file:
    date_obj=json.load(file)
    for li in date_obj:
        if "Marks" in li:
            print(li["Marks"])

json_string='{"name":"Pradeep","Roll":"1","Address":"Pune"}'
json_obj=json.loads(json_string)
#print(type(json_obj))

