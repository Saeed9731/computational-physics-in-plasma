clc;
clear;

f = @(x) (x.^3 - x.^2 + 2);

x1 = -200;
x2 = 300;

n = 0;

while (x2 - x1) > 0.01
    n = n + 1;

    if f(x1) * f(x2) > 0
        error('change the interval')
    end

    xn = (x1 + x2) / 2;

    if f(x1) * f(xn) < 0
        x2 = xn;
    else
        x1 = xn;
    end

end

disp('The root is xn = ')
disp(xn)
disp(n)
