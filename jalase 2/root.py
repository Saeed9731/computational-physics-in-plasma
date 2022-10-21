import sys


def f(x):
    return x**3-x**2+2


x1 = 1
x2 = -10

if f(x1)*f(x2) >= 0:
    sys.exit("please change the interval")
elif (x1-x2) >= 0.01:
    xn = (x1+x2)/2

if f(xn) == 0:
    pass
elif f(x1)*f(xn) < 0:
    x2 = xn
else:
    x1 = xn

print("the root is: ", "%4f" % xn)
