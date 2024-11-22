# -*- coding: utf-8 -*-
"""Linear Regression_LSM.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rWLwIzko7Brd7ewcLdsh9g-V-u9nR8l0
"""

import numpy as np #numerical python # n_Dim array
import matplotlib.pyplot as plt #plotting

x=[171,151,124,134,156]
y=[80,60,45,50,65]

#mean_x, mean_y
n=len(x)
mean_x =np.mean(x)
mean_y=np.mean(y)
print(mean_x)
print(mean_y)
#print(n)

numer=0
denom=0
for i in range(n):
  numer= numer + ((x[i]-mean_x)*(y[i]-mean_y))
  denom=denom+((x[i]-mean_x)**2)
m= numer/denom
c=mean_y -(m*mean_x)
print(m)
print(c)

plt.scatter(x,y,color="red")
plt.plot(x,y,color="blue")

max_x= np.max(x)+5
min_x= np.min(x)-5


a=np.linspace(min_x,max_x,5)
#print(a)

b=m*a+c
#print(b)
plt.scatter(x,y,color="red")
plt.plot(a,b,color="green")
plt.show()