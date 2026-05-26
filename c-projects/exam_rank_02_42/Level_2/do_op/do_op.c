#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
    if (ac != 4 && (av[2][1] != 0))
        return (write (1, "\n", 1), 0);

    int a = atoi(av[1]);
    int b = atoi(av[3]);
    int result = 0;

    if (av[2][0] == '+')
        result = a + b;
    else if (av[2][0] == '-')
        result = a - b;
    else if (av[2][0] == '*')
        result = a * b;
    else if (av[2][0] == '/')
        result = a / b;
    else
        result = a % b;

    printf("%d\n", result);

    return (0);
}