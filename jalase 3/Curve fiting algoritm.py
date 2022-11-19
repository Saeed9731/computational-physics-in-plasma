import numpy as np
import matplotlib.pylab as plt
from sympy import Symbol, lambdify


x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([0, 1, 4, 9, 16, 25, 36, 49])

m = 2

A = np.zeros((m+1, m+1), dtype=int)

n = -1
l = m-4
for i in range(m+1):
    l += 2
    for j in range(m+1):
        n += 1
        if i == 0:
            k = sum(x**(n))
            A[i, j] = k
        else:
            k = sum(x**(n-l))
            A[i, j] = k
# print(f"{A= }")

B = np.zeros((m+1, 1), dtype=int)
n = -1
for i in range(m+1):
    n += 1
    k = sum(y*x**n)
    B[i, 0] = k

# print(f"{B= }")

A_inv = np.linalg.inv(A)
theta = A_inv @ B


curv_ans = []
zarib = theta.tolist()
xs = Symbol('xs')
for i in range(m+1):
    j = zarib[i][0]
    p = j*xs**i
    curv_ans.append(p)

# print(sum(curv_ans))
Y = lambdify(xs, sum(curv_ans))
X = np.linspace(0, x[-1], 1000)

plt.scatter(x, y)
plt.plot(X, Y(X))
plt.show()
