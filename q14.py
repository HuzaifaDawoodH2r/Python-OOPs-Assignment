#Create a class Department and a class Employee. Use aggregation by having a Department object store a reference to an Employee object that exists independently of it.

class Employee:
    def __init__(self, name):
        self.name = name

    def get_details(self):
        return f"Employee Name: {self.name}"


class Department:
    def __init__(self, name, employee: Employee):
        self.name = name
        self.employee = employee  

    def get_department_info(self):
        return f"Department: {self.name}, {self.employee.get_details()}"

emp1 = Employee("Huzaifa")
dept1 = Department("HR", emp1)
print(dept1.get_department_info())  