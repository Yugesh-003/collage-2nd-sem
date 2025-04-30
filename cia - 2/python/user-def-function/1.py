#with argument with return type
def calculate(a, b):
    return a + b, a - b, a * b

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum, sub, multi = calculate(num1, num2)

print("Sum:", sum)
print(f"Subtraction: {sub}")
print(f"Multiplication: {multi}")
