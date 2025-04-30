#10.Generate a list of strings with their lengths from another list
words = ["apple", "banana", "cherry"]
lengths = [(word, len(word)) for word in words]
print(lengths)
