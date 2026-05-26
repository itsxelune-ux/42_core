#include <unistd.h>
#include <stdio.h>

char is_letter(char c)
{
    return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'));
}

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;

    while (av[1][i])
    {
        while ((av[1][i] >= 9 && av[1][i] <= 13) || (av[1][i] == ' '))
            i++;

        if (((av[1][i + 1] >= 9 && av[1][i + 1] <= 13) || (av[1][i + 1] == ' ')) && (av[1][i + 1] != '\0'))
        {
            write (1, &av[1][i], 1);
            i++;
            while ((av[1][i + 1] >= 9 && av[1][i + 1] <= 13) || (av[1][i + 1] == ' '))
                i++;
            if (av[1][i + 1] != '\0')
                write (1, "   ", 3);
        }
        else
            write (1, &av[1][i], 1);
        i++;
    }
    return (write (1, "\n", 1), 0);
}