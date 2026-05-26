#include <unistd.h>
#include <stdio.h>

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;
    char *str = av[1];
    
    while((str[i] >= 9 && str[i] <= 13) || str[i] == ' ')
        i++;
    while (str[i] && (!(str[i] >= 9 && str[i] <= 13) && str[i] != ' '))
    {
        write (1, &str[i], 1);
        i++;
    }
    return (write (1, "\n", 1), 0);
}