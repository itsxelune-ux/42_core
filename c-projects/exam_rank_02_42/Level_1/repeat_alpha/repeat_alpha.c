#include <unistd.h>
#include <stdio.h>

int assign_index(char c)
{
    if (c >= 'a' && c <= 'z')
        c = c - 'a';
    else if (c >= 'A' && c <= 'Z')
        c = c - 'A';
    return (c);

}

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;

    while (av[1][i])
    {
        if ((av[1][i] >= 'a' && av[1][i] <= 'z') || (av[1][i] >= 'A' && av[1][i] <= 'Z'))
        {
            int index = assign_index(av[1][i]);
            while (index >= 0)
            {
                write (1, &av[1][i], 1);
                index--;
            }
        }
        else    
            write (1, &av[1][i], 1);
        i++;
    }
    
    return (write (1, "\n", 1), 0);
}