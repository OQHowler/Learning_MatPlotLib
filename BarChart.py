import matplotlib.pyplot as plt  
#Plyplot is a module within the matplotlib library which provides used friendly plotting
import numpy as np

categories = np.array(["Grains", "Fruit", "Vegetables", "Protein", "Dairy", "Sweets"])
values = np.array([4, 3, 2, 5, 3, 1])

#plth.bar(categories,values)
plt.bar(categories,values)
plt.title("Daily Consumption")
plt.xlabel("Food")
plt.ylabel("Quantity")
plt.show()