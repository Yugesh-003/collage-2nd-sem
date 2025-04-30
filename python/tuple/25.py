a = (1, 2, 3, 4, 5, 6, 7, 8, 9)
b = (2, 4, 6)

print("A = ",a)
print("B = ",b)

is_subset = set(b).issubset(set(a))

if is_subset:
    print("B is a subset of A")

else:
    print("B is not a subset of A")