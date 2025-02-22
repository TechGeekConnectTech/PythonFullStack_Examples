import csv

with open("C:/Users/Mahesh Gavandar/OneDrive/Desktop/Book1.csv","r") as file:
    read_file=csv.DictReader(file)
    #for read1 in read_file:
    #    print(read1["Name"])

    read_f=csv.reader(file)
    for r in read_f:
        print(r[1])


data=[
    ["Name","Age","Result"],
    ["Praddep","31","Pass"],
    ["Prashant","10","Fail"],
]
with open("student_status.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerows(data)
    writer.writerow(("Sagar","32","Pass"))