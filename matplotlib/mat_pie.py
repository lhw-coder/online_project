import matplotlib.pyplot as plt

plt.pie([10,20,30,40],labels=list("abcd"),autopct="%.2f%%", explode=[0.3,0,0,0])
plt.axis('equal')
plt.show()