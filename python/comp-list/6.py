#6.Generate a list of pairs of numbers where the sum of each pair is prime
# Generate pairs (a, b) such that the sum is prime
pairs = [
    (a, b)
    for a in range(1, 21)
    for b in range(1, 21)
    if (a + b > 1 and all((a + b) % i != 0 for i in range(2, int((a + b)**0.5) + 1)))
]

print(pairs)
