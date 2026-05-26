#include <unistd.h>
#include <stdio.h>

char to_upper(char c)
{
    if (c >= 'a' && c <= 'z')
    {
        c = c - 32;
    }

    return (c);
}

char to_lower(char c)
{
    if (c >= 'A' && c <= 'Z')
    {
        c = c + 32;
    }

    return (c);
}

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;

    while (av[1][i])
    {
        if (av[1][i] >= 'a' && av[1][i] <= 'z')
        {
            char c = to_upper(av[1][i]);
            write (1, &c, 1);
        }
        else if (av[1][i] >= 'A' && av[1][i] <= 'Z')
        {
            char c = to_lower(av[1][i]);
            write (1, &c, 1);
        }
        else
            write (1, &av[1][i], 1);
        i++;
    }

    return (write (1, "\n", 1), 0);

}


