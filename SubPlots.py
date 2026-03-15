import matplotlib.pyplot as plt  
#Pyplot is a module within the matplotlib library which provides used friendly plotting
import numpy as np

# Ax-> a single subplot
# Figure -> entire canvas

figure,axes=plt.subplots(2,2)# 2 rows,2 columns
# axes is a numpt array

x=np.array([1,2,3,4,5])
y=np.array([5,4,3,2,1])

axes[0,0].bar(x,y,color="red")
axes[0,0].set_title("x+y=const")

axes[0,1].plot(x,y**2,color="blue")
axes[0,1].set_title("x+y=wowconst")

axes[1,0].plot(x**y,y**2,color="green")
#axes[1,0].set_title("x+y=wowconst")

plt.show()