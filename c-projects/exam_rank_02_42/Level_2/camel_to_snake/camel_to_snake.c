#include <unistd.h>
#include <stdio.h>

char to_lower(char c)
{
        return(c + 32);
}

int main(int ac, char **av)
{
    if(ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;

    while(av[1][i])
    {
        if (av[1][i] >= 'A' && av[1][i] <= 'Z')
        {
            write (1, "_", 1);
            char c = to_lower(av[1][i]);
            write(1, &c, 1);
        }
        else
            write (1, &av[1][i], 1);
        i++;
    }

    return (write (1, "\n", 1), 0);
}


