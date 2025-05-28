# 3. Public Variables and Methods
# Create a class Car with a public variable brand and a public method start(). Instantiate the class and access both from outside the class.


class Car:
    brand = "Toyota"

    def start(self):
        print("car started...")

c1 = Car()
c1.start()
print(c1.brand)