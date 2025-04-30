from matplotlib import pyplot as plt
Marks=[21,53,60,49,25,27,30,42,1,2,102,95,8,15,105,70,65,55,70,75,60,52,44,43,42,45]
bins=[0,10,20,30,40,50,60,70,80,90,100]
plt.hist(Marks, bins, histtype='bar', rwidth=0.8)
plt.xlabel('age groups')
plt.ylabel('Number of people')
plt.title('Histogram')
plt.show()