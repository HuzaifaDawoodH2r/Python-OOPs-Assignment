#Create a class decorator add_greeting that modifies a class to add a greet() method returning "Hello from Decorator!". Apply it to a class Person.

def addGreeting(cls):
    def greet(self):
        return "Hello from Decorator!"
    cls.greet = greet
    return cls

@addGreeting
class Person:
    def __init__(self, name):
        self.name = name

p = Person("Huzaifa")
print(p.greet())