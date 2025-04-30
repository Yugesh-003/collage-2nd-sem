list = [3, 4, 5, 7, 8, 9, 11]

print("The original list is ",list)
# Find the missing number
for num in range(list[0], list[-1]):
    if num not in list:
        print("Missing number:", num)
        break