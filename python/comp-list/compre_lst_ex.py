#1.Find all of the numbers from 1-1000 that are divisible by 7
divisible_by_7 = [x for x in range(1, 1001) if x % 7 == 0]
print(divisible_by_7)

#2.Find all of the numbers from 1-1000 that have a 3 in them
numbers_with_3 = [x for x in range(1, 1001) if '3' in str(x)]
print(numbers_with_3)

#3.Create a list of even numbers squared and odd numbers cubed from 1 to 10
numbers = [x**2 if x % 2 == 0 else x**3 for x in range(1, 11)]
print(numbers)

#4.Create a list of reversed strings from another list
original_list = ["apple", "banana", "cherry"]
reversed_list = [word[::-1] for word in original_list]
print(reversed_list)

#5.Create a list of numbers that are divisible by both 3 and 5 from 1 to 100
divisible_by_3_and_5 = [x for x in range(1, 101) if x % 3 == 0 and x % 5 == 0]
print(divisible_by_3_and_5)

#6.Generate a list of pairs of numbers where the sum of each pair is prime

#7.Create a list of strings with vowels replaced by asterisks
words = ["apple", "banana", "cherry"]
a= [''.join('*' if char in 'aeiouAEIOU' else char for char in word) for word in words]
print(a)

#8.Generate list of palindromes from 1 to 100
palindromes = [x for x in range(1, 101) if str(x) == str(x)[::-1]]
print(palindromes)

#9.Generate a list of positive numbers from given list
lst=[1, -2, 3, -4, 5, -6]
positive_numbers = [x for x in lst if x > 0]
print(positive_numbers)

#10.Generate a list of strings with their lengths from another list
words = ["apple", "banana", "cherry"]
lengths = [(word, len(word)) for word in words]
print(lengths)































