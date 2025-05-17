from datetime import datetime, timedelta
import csv
print(datetime.now())
print(datetime.today())
print(datetime.now().strftime("%d-%m-%y %H:%M:%S"))
print(datetime(1995,10,5))
print(datetime.today() + timedelta(days=2))
print(datetime.today() - timedelta(days=2))


data=[
    ["Id","Customer Name","Customer Address"],
    ["1","Ayush","Pune"],
    ["2","Gitanjali","Mumbai"]
]

with open("test.csv","w",newline="") as file:
    file_write=csv.writer(file)
    for d in data:
        file_write.writerow(d)
    file.close()


with open("test.csv","r") as file:
    file_read=csv.reader(file)
    for f in file_read:
        print(f)

data = [
    {"Name": "Alice", "Age": 25, "City": "New York"},
    {"Name": "Bob", "Age": 30, "City": "London"},
    {"Name": "Charlie", "Age": 28, "City": "Paris"}
]

with open('people_dict.csv', 'w', newline='') as file:
    fieldnames = ["Name", "Age", "City"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(data)

print("Dictionary CSV file written successfully!")



import csv

with open('people_dict.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)