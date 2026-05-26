#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
    int num;
    int divisor;

    if (ac != 2)
    {
        write(1, "\n", 1);
        return (0);
    }

    num = atoi(av[1]);
    divisor = 2;

    if (num == 1)
    {
        printf("1\n");
        return (0);
    }

    while (num > 1)
    {
        if (num % divisor == 0)
        {
            printf("%d", divisor);

            num = num / divisor;

            if (num > 1)
                printf("*");
        }
        else
            divisor++;
    }

    printf("\n");

    return (0);
}