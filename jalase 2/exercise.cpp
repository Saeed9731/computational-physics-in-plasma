#include <iostream>
#include <math.h>

double f(double x)
{
    return pow(x, 3) + 2 * pow(x, 2) + 3 * x + 4;
}

int main()
{
    double x1 = -200;
    double x2 = 200;
    double xn;
    if (f(x1) * f(x2) >= 0)
    {
        std::cout << "please change the interval!!!! \n";
        exit(0);
    }
    do
    {
        xn = (x1 + x2) / 2;
        if (f(xn) == 0)
        {
            break;
        }
        else if (f(x1) * f(xn) < 0)
        {
            x2 = xn;
        }
        else
        {
            x1 = xn;
        }

    } while ((x2 - x1) >= 0.01);
    std::cout << "the root is: " << xn;
    return 0;
}