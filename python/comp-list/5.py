#5.Create a list of numbers that are divisible by both 3 and 5 from 1 to 100
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)
