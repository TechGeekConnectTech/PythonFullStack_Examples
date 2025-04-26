'''
def functionname(<args1>,<args2>,..):
    statement
    return


return_vaule=functionname(<args1>,<args2>,..)
'''
'''
#without args
def isodd(number):
    if number%2 == 0:
        return False
    else:
        return True



#pass argument concatinate function
def concatinate(string1,string2):
    return string1+string2

print(concatinate("Ayush","Lakde"))
'''


def diffOddEven(num_list):
    if len(num_list) == 0:
        return None
    odd=[]
    even=[]
    for num in num_list:
        if num%2 == 0:
            even.append(num)
        else:
            odd.append(num)

    return odd,even

