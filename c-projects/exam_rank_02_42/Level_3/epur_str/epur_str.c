#include <stdio.h>
#include <unistd.h>

int main (int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;

    while ((av[1][i] >= 9 && av[1][i] <= 13) || av[1][i] == ' ')
        i++;

    int begin = i;

    while (av[1][i])
        i++;

    i--;
    while ((av[1][i] >= 9 && av[1][i] <= 13) || av[1][i] == ' ')
        i--;
    int end = i;

    i = begin;

    while (i <= end)
    {
        if ((av[1][i] >= 9 && av[1][i] <= 13) || av[1][i] == ' ')
        {
            write (1, " ", 1);
            while ((av[1][i] >= 9 && av[1][i] <= 13) || av[1][i] == ' ')
                i++;
            i--;
        }
        else
            write (1, &av[1][i], 1);
        i++;  
    }
    return (write (1, "\n", 1), 0);
}