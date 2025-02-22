def addition(number1,number2):
    sum=number1+number2
    return sum

def subsraction(number1,number2):
    sub=number1-number2
    return sub

def student(name,greeting="Hello"):
    return name +" "+greeting


'''
#Paramter function example
def addition(number1,number2):
    sum=number1+number2
    print(f"Sum of number is : {sum}")
'''
'''
#Return function example
def addition(number1,number2):
    sum=number1+number2
    return sum

#Set Default Paramter of function
def addition(number1,number2=40):
    sum=number1+number2
    return sum
'''


'''
if __name__ == "__main__":
    addition()


    addition(10, 20)
    addition(30, 40)

    add = addition(10, 20)
    sum = addition(add, 90)
    print(f"Addition is number : {sum}")

    add = addition(10, 10)
    sum = addition(add, 90)
    print(f"Addition is number : {sum}")
'''