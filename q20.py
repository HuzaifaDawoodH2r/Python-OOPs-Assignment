#Create a custom exception InvalidAgeError. Write a function check_age(age) that raises this exception if age < 18. Handle it with try...except.

class InvalidAgeError(Exception):
    def __init__(self, message = "Age must be 18 or older."):
        super().__init__(message)

def checkAge(age):
    if  age < 18:
        raise InvalidAgeError(f"Invalid age {age} must be 18 or older.")
    else:
        print("Age is valid")
        print("Your are older")

try:
    userAge = int(input("Enter your age: "))
    checkAge(userAge)
except InvalidAgeError as e:
    print(e)

    