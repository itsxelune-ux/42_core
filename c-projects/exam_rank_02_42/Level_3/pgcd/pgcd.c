#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main(int ac, char **av)
{
    if (ac != 3)
        return (write (1, "\n", 1), 0);

    int a = atoi(av[1]);
    int b = atoi(av[2]);

    while (b != 0)
    {
        unsigned int temp = b;
        b = a % b;
        a = temp;
    }

    printf("%d", a);
    printf("\n");
}