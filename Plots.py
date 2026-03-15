import matplotlib.pyplot as plt  
#Plyplot is a module within the matplotlib library which provides used friendly plotting

x = [2023,2024,2025,2026]
y1=[80,90,50,70]
y2=[90,100,90,90]

# Making a graph and showing it,pretty self-explanatory
plt.plot(x,y1, marker="v",
              markersize=20,
              markerfacecolor="blue",
              markeredgecolor="red",
              linestyle="dashed",# can set it to none
              linewidth=5,
              color="green"
              )

plt.title("Class size", fontsize=25,
          family="Arial",
          fontweight="bold",
          color="#2d4cfc")

plt.xlabel("Year",fontsize=15,family="Arial",fontweight="bold")
plt.ylabel("Performance",fontsize=15,family="Arial",fontweight="bold")

plt.xticks(x) #makes x axis exaclty as the array

plt.tick_params(axis="both", colors="#2dbefc")


plt.grid(axis="x",linewidth=2,color="red")
plt.grid(axis="y",linewidth=1,color="green",linestyle="dashed")

plt.plot(x,y2)
plt.show()