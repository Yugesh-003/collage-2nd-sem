#Make a dictionary of student names and their scores. 
# Write a function to find the student with the highest score.
s = {"Yugesh":100, "Venki":90, "Abi":80, "Gayathri":99}

high_mark_std = max(s, key=s.get)
highest_score = s[high_mark_std]

print(high_mark_std)