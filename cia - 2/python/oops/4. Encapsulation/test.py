nums = [1,2,3,4,5,6]

prime = {x : (False if x < 2 else all(x % i != 0 for i in range(2,int(0.5**x)+1))) for x in nums}

print(prime)