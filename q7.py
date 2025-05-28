#Create a class Employee with:
#a public variable name,
#a protected variable _salary, and
#a private variable __ssn.
#Try accessing all three variables from an object of the class and document what happens.

class Employee:
    def __init__(self, name, salary, ssn):
        self.name = name
        self._salary = salary
        self.__ssn = ssn

e1 = Employee("Huzaifa", "6,000$", 123_456_789)

print("name = ",e1.name)
print("salary = ",e1._salary)
try:
    print(e1.__ssn)
except AttributeError as e:
    print ("SSN = ", "Social Security Number Is Private")