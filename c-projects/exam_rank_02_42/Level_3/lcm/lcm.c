#include <unistd.h>
#include <stdio.h>

unsigned int gcm(unsigned int a, unsigned int b)
{

    while (b != 0)
    {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return (a);
}

unsigned int    lcm(unsigned int a, unsigned int b)
{
    if (a == 0 || b == 0)
        return (0);
    return (a / gcm(a, b) * b);
}