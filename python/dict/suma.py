#to accept n numbers from the user and print the factorial of every odd numeber
import math

numbers = list(map(int, input("Enter numbers separated by commas: ").split(',')))

x = [math.factorial(var) for var in numbers if var % 2 != 0 ]

print(x)