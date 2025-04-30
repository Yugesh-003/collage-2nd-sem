#1.Filter set elements greater than 25 using set comprehension
set = {12, 34, 56, 3, 45, 67, 89, 1, 6}
filter = {x for x in set if x > 25}
print(filter)
