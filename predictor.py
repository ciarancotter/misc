import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import linregress
x = np.array([2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019])
y = np.array([300, 290, 300, 300, 300, 300, 300, 300, 315, 330, 340, 425, 430, 440, 435, 419, 398, 402])

x_2 = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019])
y_2 = np.array([425, 430, 440, 435, 419, 398, 402])

stats = linregress(x_2, y_2)
m = stats.slope
b = stats.intercept

yVal = m * 2020 + b
plt.scatter(x_2, y_2)
plt.plot(x_2, m * x_2 + b, color = "red")
plt.show()
print(2020, yVal)

