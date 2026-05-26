#include <unistd.h>

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    char *str = av[1];
    int i = 0;
    int end;

    while (str[i])
        i++;

    i--;

    while (str[i])
    {
        end = i;
        
        while(av[1][i] && ((str[i] >= 9 && str[i] <= 13) || str[i] == ' '))
            i--;
        
        while(av[1][i] && (!(str[i] >= 9 && str[i] <= 13) && str[i] != ' '))
            i--;

        write(1, &str[i + 1], end - i);
        write(1, " ", 1);
        i--;
    }
    return (write (1, "\n", 1), 0);
}