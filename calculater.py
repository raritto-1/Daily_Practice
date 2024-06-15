class Calculator:
    def add(self, x, y):
        return x + y

    def subtract(self, x, y):
        return x - y

    def multiply(self, x, y):
        return x * y

    def divide(self, x, y):
        if y != 0:
            return x / y
        else:
            raise ValueError("Cannot divide by zero.")

calculator = Calculator()

result_add = calculator.add(5, 3)
result_subtract = calculator.subtract(8, 4)
result_multiply = calculator.multiply(2, 6)
result_divide = calculator.divide(10, 2)

print("Addition:", result_add)
print("Subtraction:", result_subtract)
print("Multiplication:", result_multiply)
print("Division:", result_divide)
