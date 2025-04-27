class ElectionError(Exception):
    pass

def check_eligibility(age):
    if int(age) > 18:
        return True
    else:
        raise ElectionError("Person is not Eligible for creating election Card")

if __name__ == '__main__':
    age=input("Enter your Age?")
    try:
        if check_eligibility(age):
            print("Person is Eligible")
    except Exception as e:
        print(e)


