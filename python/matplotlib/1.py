import matplotlib.pyplot as plt

plt.title("Line Graph")

plt.plot([1,4,5],[5,3,2],'r',linewidth=2,label="Line1")

plt.legend()
plt.grid(True)
plt.show()