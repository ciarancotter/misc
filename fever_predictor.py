import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
x = np.array([0, 22.433, 35.83, 39.58, 40.58, 44.33])
y = np.array([38.3, 38.3, 38.3, 37.5, 37.7, 37.4])


stats = linregress(x, y)
m = stats.slope
b = stats.intercept


yVal = m * 45.33 + b
plt.scatter(x, y)
plt.xlabel("Hours since fever began")
plt.ylabel("Body temperature")
plt.title("Linear regression of Covid-19 symptoms")
plt.plot(x, m * x + b, color = "red")
plt.savefig('graph.jpg')
plt.show()

print("Next:", yVal)


