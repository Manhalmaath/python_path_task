class Calculator:
    def __init__(self, val):
        self.val = val

    def __add__(self, other):
        return self.val + other.val

    def __sub__(self, other):
        return self.val - other.val

    def __mul__(self, other):
        return self.val * other.val

    def __truediv__(self, other):
        return self.val / other.val

    def __str__(self):
        return f"{self.val}"


num1 = Calculator(5)
num2 = Calculator(10)
print(num1 + num2)
print(num1 - num2)
print(num1 * num2)
print(num1 / num2)
