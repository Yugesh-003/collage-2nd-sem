
#8.Generate a set of tuples containing numbers and their squares for even numbers
evensqr = {(x, x**2) for x in range(1, 11) if x % 2 == 0}
print(evensqr)
