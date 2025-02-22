try:
    file=open("college.txt","r")
    file.read()
except FileNotFoundError as e:
    print(f"File Not Found : {e}")
finally:
    print("Finally Block is always execute whether exception is occured o not")
    file.close()