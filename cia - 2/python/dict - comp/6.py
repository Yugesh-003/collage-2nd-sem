num = [1,2,3,4,5,6,7]

prime={x:(False if x < 2 else all (x%i != 0 for i in range(2,int(x**0.5)+1))) for x in num}

print(prime)