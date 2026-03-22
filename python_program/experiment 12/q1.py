#1.WAP to plot a simple graph using plot().
import matplotlib.pyplot as plt
x = [1, 2, 3, 4]
y = [10, 20, 25, 30]
plt.plot(x, y)
plt.title("Simple Line Plot")
plt.plot(x, y, linestyle='--', color='r', marker='o', label="Data Line")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.grid()
plt.show()



#2.WAP to draw the scatter and bar plot.
x = [1, 2, 3, 4, 5]
y = [5, 7, 6, 8, 7]
plt.scatter(x, y, color='b', label="Scatter Points")
plt.title("Scatter Plot")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.legend()
plt.show()

categories = ['A', 'B', 'C', 'D']
values = [3, 7, 8, 5]
plt.bar(categories, values, color='g', 
label="Bar Data")
plt.title("Bar Plot")
plt.xlabel("Categories")
plt.ylabel("Values")
plt.legend()
plt.show()


#3.WAP to draw Histograms and Box plots.
data = [22, 87, 5, 43, 56, 73, 55, 54, 
11, 20, 51, 5]
plt.hist(data, bins=5, color='purple', 
label="Histogram Data")
plt.title("Histogram")


data = [7, 8, 5, 6, 9, 10, 15, 20, 21]
plt.boxplot(data)
plt.title("Box Plot")
plt.show()
plt.xlabel("Bins")
plt.ylabel("Frequency")
plt.legend()
plt.show()




#4.WAP to draw Pie Charts and Contour plots.
sizes = [15, 30, 45, 10]
labels = ['A', 'B', 'C', 'D']
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue']
explode = (0, 0.1, 0, 0) # Explode 2nd slice
plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', 
shadow=True, startangle=140)
plt.title("Pie Chart")
plt.axis('equal')
plt.show()



import numpy as np
x = np.linspace(-5, 5, 50)
y = np.linspace(-5, 5, 50)
X, Y = np.meshgrid(x, y)
Z = np.sin(np.sqrt(X**2 + Y**2))
plt.contour(X, Y, Z, levels=10, cmap='viridis')
plt.title("Contour Plot")
plt.colorbar()
plt.show()



#5.WAP to draw the 3D-plot.
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x = [1, 2, 3, 4, 5]
y = [5, 6, 7, 8, 9]
z = [2, 3, 3, 3, 2]
ax.scatter(x, y, z, color='r', label="3D Points")
ax.set_title("3D Scatter Plot")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Z-axis")
plt.legend()
plt.show()