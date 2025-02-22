#Arithmetic Operator
from ctypes import PyDLL
from multiprocessing.process import ORIGINAL_DIR

number1=2
number2=16

print(number1+number2)
print(number2-number1)
print(number2/number1)
print(number2*number1)
print(number1**number2)    #2*2*2*2*2...2
print(number2%number1)


#Comparision Operator
number1=2
number2=16

print(number1>number2)
print(number1<number2)
print(number1>=number2)
print(number1<=number2)
print(number1!=number2)
print(number1==number2)

#Logical Operator
#Python  ShellScript
#and  -- &&
#or -- ||
#not -- !

title="welcome, to our Python Fullstack Class"
list=title.split(" ")
if "Python" in list and "Java" in list:
    print("present")
else:
    print("Not Present")

if "Python" in list or "Java" in list:
    print("present")
else:
    print("Not Present")

if "Python" in list and "Class" in list:
    print("present")
else:
    print("Not Present")

if "Shell Script" not in list and ".Net" not in list:
    print("Not present")

a=10
b=10

print(a is not b)