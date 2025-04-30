# Create a nested dictionary of three employees, each with keys for name, age, and
# salary. Write a function to give each employee a 10% raise and print the updated
# dictionary.
employees = {
    "employee1": {"name": "Papu", "age": 30, "salary": 15000},
    "employee2": {"name": "Kanna", "age": 40, "salary": 16000},
    "employee3": {"name": "Charu", "age": 35, "salary": 15500}
}

for employee in employees.values():
    employee["salary"] *= 1.10  
    
for i in employees:
    print(employees[i])

