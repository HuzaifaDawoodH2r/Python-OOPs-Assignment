#Create a class Dog with instance variables name and breed. Add an instance method bark() that prints a message including the dog's name.

class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.breed} {self.name} says woof! woof!")

dog = Dog("German Shepherd","Golden Retriever -")
dog2 = Dog("Husky","Dachshund -")
dog.bark()
dog2.bark()