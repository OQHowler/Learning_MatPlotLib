import matplotlib.pyplot as plt  
#Plyplot is a module within the matplotlib library which provides used friendly plotting
import numpy as np

use=["sleep","study","class","timepass"]
values=[8,8,4,4]
colors1=["red","yellow","green","blue"]
plt.pie(values,labels=use,
               autopct="%1.0f%%",
               colors=colors1,
               explode=[0.03,0.03,0.03,0.2],
               shadow=False,
               startangle=35
        )

plt.title("Time usage")
plt.show()