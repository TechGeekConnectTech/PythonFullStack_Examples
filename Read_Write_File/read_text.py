'''

with open("industry.txt") as file_o:
    content=file_o.read()
    print(content)
    file_o.close()

with open("industry.txt","r") as file_obj:
      for line in file_obj:
          if line.strip() in ["Automotive","Banking/Mortgage","Clerical/Administrative"]:
              print(line)
      file_obj.close()

with open("industry.txt") as file_obj:
    print(file_obj.readable())
    file_obj.close()

'''
with open("industry.txt") as file_obj:
    print(file_obj.readlines())
    print("is file writable or not",file_obj.writable())
    print("if file readable or not",file_obj.readable())
'''
with open("industry.txt") as file_obj:
    print(file_obj.readlines()[2:10])
    file_obj.close()

list_obj=[]
with open("industry.txt", "r") as file_obj:
    for line in file_obj:
        list_obj.append(line)

    file_obj.close()

print(list_obj)
'''