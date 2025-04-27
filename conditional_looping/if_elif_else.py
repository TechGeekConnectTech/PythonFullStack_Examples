''''
# Check number if odd or even
if <condition>: #if condition is satisfied then execute statement
     statement
elif <condition>:  #check if above condition is not match, then chekc this condition if match then execute
    statement
else:     #if none of condition satisfied then execute  else block
    statement
'''
'''
#check number if odd or even
number=input("Enter Number : ")
if int(number) % 2 == 0:
    print("Number is even")
else:
    print("Number is odd")
'''

#Hire candidates, based on below parameter
#condition 1 - Person should be ready to relocate in Pune or Mumbai Location
#condition 2 - Person salary should not be greater than 30
#condition 3 - Person experience should be more than 10 years

location="Delhi"
salary=12
experience=11

if location == "Pune" or location == "Mumbai" and salary < 30 and experience > 10:
    print("Process for interview")
else:
    print("Reject candidates")


#Information about couse
course_name="Python"
crashcourse=False

if course_name == "Python":
    print("Welcome to Python Course")
    if crashcourse:
        print("Crash course duration 2 month")
    else:
        print("Full course duration 6 month")
elif course_name == "Devops":
    print("Welcome to Devops Course, Course duration is 3+ month")
elif course_name == "Java":
    print("Welcome to Java Course, Course duration is 6+ month")
else:
    print("We don't have such course available")

#