from matplotlib import pyplot as plt
x=["Jithu","Kanna","Charu"]
y=[78,55,60]
ex=[0.1,0,0]
colors=["Gold","Silver","cyan"]
plt.pie(y,ex,labels=x,colors=colors,autopct='%1.1f%%',shadow=True,startangle=90)
plt.title("Pie Chart")
plt.legend(loc="lower left")
plt.show()