import json
from xml.etree.ElementTree import indent

jsonstring= {
    "Name": "Mahesh",
    "Roll": 2,
    "Address": "Pune"
}
print(jsonstring)
json_data=json.dumps(jsonstring,indent=4,sort_keys=True)
print(json_data)

with open("jsonfile.json","w") as file:
    file.write(json_data)

with open("jsonfile.json","r") as file:
    load_date=json.load(file)
    print(load_date)

json_data =  '{"Name": "Mahesh", "Roll": 2, "Address": "Pune"}'
print(json.loads(json_data))