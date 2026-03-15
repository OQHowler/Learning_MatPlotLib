import matplotlib.pyplot as plt  
#Pyplot is a module within the matplotlib library which provides used friendly plotting
import numpy as np
import pandas as pd

df=pd.read_csv("poke_data.csv")

#returns number of each category
print(df["Type 1"].value_counts())

#putting it inside a series
type_count=df["Type 1"].value_counts(ascending=True)

plt.barh(type_count.index,type_count.values,color="red",edgecolor="black")
plt.title("Pokemon by type counts")
plt.xlabel("count")
plt.ylabel("number")

# to make sure it fits
plt.tight_layout()
plt.show()