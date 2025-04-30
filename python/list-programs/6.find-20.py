lst = [5, 10, 15, 20, 25, 50, 20]

print("Actual list : ",lst)

# Check if 20 is in the list
if 20 in lst:
    index = lst.index(20)
    lst[index] = 200

print("Updated list:", lst)