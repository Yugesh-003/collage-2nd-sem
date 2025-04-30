#Write a python program to illustrate a function that accepts 2 values and return its sum, subtraction and multiplication.(pass argument and return value)

def calculate(a, b):
    return a + b, a - b, a * b

# Example usage
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

sum, sub, multi = calculate(num1, num2)

print(f"Sum: {sum}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {multi}")
