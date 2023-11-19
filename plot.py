import matplotlib.pyplot as plt
import math

n=4
theta=3/4
values = []
xaxis = []
for y in range(n+1):
    curr = math.factorial(n)/(math.factorial(y)*math.factorial(n-y))*(theta**y)*((1-theta)**(n-y))
    values.append(curr)
    xaxis.append(y)

plt.bar(xaxis,values)
plt.ylabel('Likelihood p(y|theta=0.75, n=4)')
plt.xlabel('y')
plt.show()