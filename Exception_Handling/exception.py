#number=10
#print(number/0)


try:
    file_name=open("xvz.txt","w")
    file_name.read()
except ZeroDivisionError as e:
    print("Zero Division Error: {0}".format(e))
except ValueError as e:
    print("Value Error Exception: {0}".format(e))
except FileNotFoundError as e:
    print("File not Present Exception: {0}".format(e))
except Exception as e:
    print("Unknown  Error because: {0}".format(e))
finally:
    file_name.close()

print("This is we have to print")
