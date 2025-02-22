import sys


def check_age(age):
    if age < 18:
        raise ValueError("Age Can't be less than 18 years")
    else:
        return "Person is eligible for election card"

if __name__ == "__main__":
    try:
        print(check_age(16))
    except ValueError as e:
        print(e)

    print("I'm storing person details into Database")