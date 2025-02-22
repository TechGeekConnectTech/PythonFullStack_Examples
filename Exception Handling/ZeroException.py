number=10
division=0

try:
    division=number/10
except ZeroDivisionError as e:
    print(f"Number can;t be divide by zero : {e}")
else:
    print(f"Division is : {division}")

name="1234"
try:
    int(name)
except ValueError as e:
    print(f"String can't convert to Integer : {e}")
else:
    print(f"String can be convert into Integrer : {int(name)}")


number=20
try:
    division=number/0
    int("Gitanjali")
except Exception as e:
    print(f"I'm in Parent Exception : {e}")
except ZeroDivisionError as e:
    print(f"Number can;t be divide by zero : {e}")
except ValueError as e:
    print(f"String can't convert to Integer : {e}")
