from typing import final

number=10
name="Ayush"
try:
    division=number/10
    int(name)
except ZeroDivisionError as e:
    print(f"Number can't divide by zero : {e}")
except ValueError as e:
    print(f"Value error exception throw : {e}")
else:
    print(f"Division of number is : {division}")
finally:
    print("I'm always executing")