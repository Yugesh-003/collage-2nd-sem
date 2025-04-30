#without arrgument with return type

def calculate():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a+b, a-b, a*b    

# Example usage

sum, sub, multi = calculate()

print(f"Sum: {sum}")
print(f"Subtraction: {sub}")
print(f"Multiplication: {multi}")
