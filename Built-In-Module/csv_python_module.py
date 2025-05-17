import csv
'''
car=[
    ["CarName","CarManufacture","CarSegment"],
    ["Ciaz","Maruti","Sedan"],
    ["Thar","Mahindara","SUV"],
    ["I10","Hyundai","Hatchback"]
]
with open("car.csv","w",newline="") as file_name:
    writer=csv.writer(file_name)
    #writer.writerows(car)
    for row in car:
        writer.writerow(row)


with open("car.csv","r") as file_name:
    reader=csv.reader(file_name)
    for row in reader:
        print(row[0],row[2])
'''

dict_obj=[
    {"CarName":"Ciaz","CarManufacture":"Maruti","CarSegment":"Sedan"},
    {"CarName":"Thar","CarManufacture":"Mahindara","CarSegment":"SUV"},
    {"CarName":"I10","CarManufacture":"Hyundai","CarSegment":"Hatchback"}
]
with open("car_new.csv","w",newline="") as file:
    field=["CarName","CarManufacture","CarSegment"]
    writer=csv.DictWriter(file,field)
    writer.writeheader()
    writer.writerows(dict_obj)


with open("car_new.csv","r",newline="") as file:
    reader=csv.DictReader(file)
    for row in reader:
        print(row)