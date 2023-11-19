import matplotlib.pyplot as plt
import math
import numpy as np

n=1
y=1
values = []
xaxis = []
for theta in np.arange(0, 1.05, 0.05):
    curr = math.factorial(n)/(math.factorial(y)*math.factorial(n-y))*(theta**y)*((1-theta)**(n-y))
    values.append(curr)
    xaxis.append(theta)

plt.plot(xaxis, values)
plt.title('Posterior after 1 head (n=1, y=1)')
plt.ylabel('Posterior distribution of theta')
plt.xlabel('theta')
plt.show()