# Create a class MathUtils with a static method add(a, b) that returns the sum. No class or instance variables should be used.

class MathUtils:
    @staticmethod
    def add(a, b):
        return a + b
    
ans = MathUtils()
print("5 + 8 =",ans.add(5, 8))