import matplotlib.pyplot as plt
from scipy.sparse import csgraph
from scipy.integrate import odeint
import numpy as np
from numpy import array, dot, pi
import random
def deriv(x,t):            
    return dot(-L,x)
s = (60,60)
A = np.zeros(s)
for i in range(59):
    A[i][i+1]=1
    A[i+1][i]=1
A[0][59]=1
A[59][0]=1
print(A)
L = csgraph.laplacian(A, normed=False)
t = np.linspace(0, 100, 200)
s = (1, 60)
x0 = np.zeros(s)

for i in range(60):
    x0[0][i]=random.uniform(-5.0, 5.0)
x0 = x0.reshape(-1);
MA = odeint(deriv, x0, t)
for i in range(60):
    plt.plot(t,MA[:,i])
plt.title('Bucky')
plt.xlabel('Thoi gian[x]')
plt.ylabel('Bien trang thai x_i(t)')
plt.show()

