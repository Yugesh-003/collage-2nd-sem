num = [1,2,3,4,5,6,7]
prime={x:(False if x < 2 else all (x%i != 0 for i in range(2,x)))for x in num}
print(prime)



#{x:(False if x < 2 else all(x%i != 0 for i in range(2,x)))for x in num}