import matplotlib.pyplot as plt  
#Plyplot is a module within the matplotlib library which provides used friendly plotting
import numpy as np

# Generation of random scores
scores=np.random.normal(loc=70,scale=10,size=100)
# loc is the mean of the desired data
# scale is the standard deviation of the desired data

# to make sure that no score got above 100 or below 0
scores=np.clip(scores,0,100)

plt.hist(scores, bins=10,
         color="lightgreen",
         edgecolor="black")



plt.show()