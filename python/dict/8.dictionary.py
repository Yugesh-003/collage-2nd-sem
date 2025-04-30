#Get the key of a minimum &amp; maximum value from the following dictionary
sample_dict = {'Physics': 82, 'Math': 65, 'history': 75}

minimum = min(sample_dict, key=sample_dict.get)

maximum = max(sample_dict, key=sample_dict.get)

print("Minimum value:", minimum)
print("Maximum value:", maximum)
