#include <iostream>
#include <math.h>

double f(int x)
{
    return pow(x, 3) - pow(x, 2) + 2;
}

int main()
{
    double x1 = 1;
    double x2 = -10;
    double xn;
    if (f(x1) * f(x2) >= 0)
    {
        std::cout << "please change the interval!!!! \n";
        exit(0);
    }
    else if ((x1 - x2) >= 0.1)
    {
        xn = (x1 + x2) / 2;
    }
    // .........................
    if (f(xn) == 0)
    {
        exit(0);
    }
    else if (f(x1) * f(xn) < 0)
    {
        x2 = xn;
    }
    else
    {
        x1 = xn;
    }

    std::cout << "the root is: " <<xn;
    return 0;
}