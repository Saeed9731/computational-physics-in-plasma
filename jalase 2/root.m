clc;
clear;
syms x

f = input('f(x)= ');
x1 = input('x1= ');
x2 = input('x2= ');
e = input('e= ');
f = inline(f);

if f(x1) * f(x2) > 0
    error('change the interval')
end

n = 0;
xn = (x1 + x2) / 2;

while abs(f(xn)) > e
    n = n + 1;

    if f(x1) * f(xn) > e
        x2 = xn;
    else
        x1 = xn;
    end

    xn = (x1 + x2) / 2;
end

display('The root is xn = ', xn)
