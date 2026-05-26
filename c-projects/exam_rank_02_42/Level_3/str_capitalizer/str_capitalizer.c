#include <stdio.h>
#include <unistd.h>

char is_letter(char c)
{
    return ((c >= 'a' && c <= 'z') || (c >= 'A' && c <= 'Z'));
}

char to_upper(char c)
{
    if (c >= 'a' && c <= 'z')
        c = c - 32;
    return(c);
}

char to_lower(char c)
{
    if (c >= 'A' && c <= 'Z')
        c = c + 32;
    return(c);
}

void str_cap(char *str)
{
    int i = 0;

    while (str[i])
    {
        if (is_letter(str[i]))
        {
            if ((str[i - 1] >= 9 && str[i - 1] <= 13) || (str[i - 1] == ' ') || (str[i - 1] == 0))
            {
                char c = to_upper(str[i]);
                write (1, &c, 1);
            }
            else
            {
                char c = to_lower(str[i]);
                write (1, &c, 1);
            }
        }
        else
            write (1, &str[i], 1);
        i++;
    }
}


int main(int ac, char **av)
{
    if (ac < 2)
        return (write (1, "\n", 1), 0);

    int i = 1;

    while (i < ac)
    {
        str_cap(av[i]);
        i++;
        write (1, "\n", 1);
    }

    return (0);
}