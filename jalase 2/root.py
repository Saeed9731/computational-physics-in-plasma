import sys


def f(x):
    return x**3-x**2+2


x1 = -200
x2 = 300


if f(x1)*f(x2) >= 0:
    sys.exit("please change the interval")

while (x2-x1) >= 0.01:
    xn = (x1+x2)/2
    if f(xn) == 0:
        break
    elif f(x1)*f(xn) < 0:
        x2 = xn
    else:
        x1 = xn

print("the root is: ", "%4f" % xn)
