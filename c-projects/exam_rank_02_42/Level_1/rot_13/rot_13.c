#include <stdio.h>
#include <unistd.h>

char is_letter(char c)
{
    return ((c >= 'a' && c <= 'Z') || (c >= 'A' && c <= 'Z'));
}

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    
    char *str = av[1];
    int i = 0;

    while (str[i])
    {
        if ((str[i] >= 'a' && str[i] <= 'z') || (str[i] >= 'A' && str[i] <= 'Z'))
        {
            char c;

            if ((str[i] >= 'a' && str[i] <= 'm') || (str[i] >= 'A' && str[i] <= 'M'))
            {
                c = str[i] + 13;
                write (1, &c, 1);
            }
            else
            {
                c = str[i] - 13;
                write (1, &c, 1);
            }
        }
        else
            write (1, &str[i], 1);
        i++;
    }


    return (write (1, "\n", 1), 0);
}