#include <unistd.h>
#include <stdio.h>

int ft_len(char *str)
{
    int i = 0;
    while (str[i])
        i++;

    return (i);
}

char    *ft_strrev(char *str)
{
    int len = ft_len(str);

    int i = 0;
    int temp;

    while (i < len / 2)
    {
        temp = str[i];
        str[i] = str[len - 1 - i];
        str[len - 1 - i] = temp;
        i++;

    }

    return (str);
}