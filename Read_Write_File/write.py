'''
with open("industry.txt") as read_obj:
    with open("prefered_industry.txt","w") as write_obj:
        for line in read_obj:
            if "Business" in line:
                write_obj.write(line)

write_obj.close()
read_obj.close()
'''

'''
with open("industry.txt") as read_obj:
    with open("writable.txt","w") as write_obj:
        write_obj.writelines(read_obj.readlines())


with open("new_file","a") as write_obj:
    students=["Ajay\n","Ranjiv\n","Gitanjali\n","Mahesh\n"]
    write_obj.writelines(students)

with open("new_file","a") as write_obj:
    students=["Ajay\n","Ranjiv\n","Gitanjali\n","Mahesh\n"]
    for student in students:
        write_obj.write(student)

'''
with open("industry.txt") as read_obj:
    with open("writable.txt","a") as write_obj:
        write_obj.write("\n")
        for line in read_obj:
            if "Business" in line:
                write_obj.write(line)
