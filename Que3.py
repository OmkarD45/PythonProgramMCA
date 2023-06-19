'''
Write python program for +, -, operator overloading(take user input)
'''
class Number:
    def __init__(self, value):
        self.value = value

    def __add__(self, other):
        if isinstance(other, Number):
            return Number(self.value + other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value + other)
        else:
            return NotImplemented

    def __sub__(self, other):
        if isinstance(other, Number):
            return Number(self.value - other.value)
        elif isinstance(other, (int, float)):
            return Number(self.value - other)
        else:
            return NotImplemented

    def __str__(self):
        return str(self.value)


# Example usage:
num1 = Number(float(input("Enter the first number: ")))
num2 = Number(float(input("Enter the second number: ")))

result1 = num1 + num2
result2 = num1 - num2

print("Addition result:", result1)
print("Subtraction result:", result2)
