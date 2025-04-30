tup = (1, 2, 3, 4, 5, 6, 7, 8, 9)

print(tup)

even = 0
odd = 0

for num in tup:
    if num % 2 == 0:
        even += 1
    else:
        odd += 1

print("Count of,")
print("Even numbers:", even)
print("Odd numbers:", odd)
