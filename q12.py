#Create a class TemperatureConverter with a static method celsius_to_fahrenheit(c) that returns the Fahrenheit value.

class TemperatureConverter:
    @staticmethod
    def celsius_to_fahrenheit(c):
        return (c * 9/5) + 32


c = 25
temp_f = TemperatureConverter()
print("C =", c, "To Convert F =", temp_f.celsius_to_fahrenheit(c))