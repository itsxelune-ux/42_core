#include <unistd.h>
#include <stdio.h>

int main(int ac, char **av)
{
    if (ac != 3)
        return (write (1, "\n", 1), 0);

    int i = 0;
    int j = 0;

    while (av[1][i] && av[2][j])
    {
        if (av[1][i] == av[2][j])
            i++;
        j++;
    }

    if (av[1][i] == '\0')
    {
        write (1, "1\n", 2);
        
    }
    else
        write (1, "0\n", 2);

    return (0);
}