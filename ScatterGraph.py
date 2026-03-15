import matplotlib.pyplot as plt  
#Plyplot is a module within the matplotlib library which provides used friendly plotting
import numpy as np

x1=[0,1,2,3,4,1,3,6,7,3,5]
y1=[58,67,32,34,25,32,34,25,45,61,73]

x2=[1,2,7,1,6,2,8,3,5,6,2]
y2=[32,34,25,45,61,72,39,34,58,67,48]

plt.scatter(x1, y1,
            color="skyblue",
            alpha=0.5,
            s=200,
            label="class1")
plt.scatter(x2, y2,
            color="red",
            alpha=0.5,
            s=200,label="class2")

plt.xlabel("Hours Studied")
plt.ylabel("Grades")
plt.title("Test Scores")
plt.legend()
plt.show()