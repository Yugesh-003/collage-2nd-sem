#10.Check for palindrome words
words = ['level', 'radar', 'python', 'world', 'madam']
palin = {word for word in words if word == word[::-1]}
print(palin)