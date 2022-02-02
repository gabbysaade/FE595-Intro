# Introduction Assignment
# Use matplotlib and numpy to create a graph of one period of sin(x) and cos(x) on the same set of axes

# Import necessary packages
import numpy as np
import matplotlib.pyplot as plt

# Create array of values for the sin graph
x = np.arange(0, 2 * np.pi, 0.1)
y = np.sin(x)
z = np.cos(x)

# Create and show plot with title, axis labels, and legend
plt.plot(x, y, x, z)
plt.title('Plot of One Period of sin and cos')
plt.xlabel('Values of x from 0 to 2pi')
plt.ylabel('Corresponding Values of sin(x) and cos(x)')
plt.legend(['sin(x)', 'cos(x)'])
plt.show()
