clc;
clear;
syms x

f = input('f(x)= ');
x1 = input('x1= ');
x2 = input('x2= ');
f = inline(f);

if f(x1) * f(x2) > 0
    error('change the interval')
end

n=0
xn=(x1+x2)/2
