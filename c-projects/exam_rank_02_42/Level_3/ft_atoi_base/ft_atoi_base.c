#include <stdio.h>
#include <unistd.h>

int     ft_atoi_base(const char *str, int str_base)
{
    int value;
    int result = 0;
    int sign = 1;
    int i = 0;

    while ((str[i] >= 9 && str[i] <= 13) || str[i] == ' ')
        i++;

    if (str[i] == '+' || str[i] == '-')
    {
        if (str[i] == '-')
            sign = -1;
        i++;
    }

    while (str[i])
    {
        if (str[i] >= '0' && str[i] <= '9')
            value = str[i] - '0';
        else if (str[i] >= 'a' && str[i] <= 'f')
            value = str[i] - 'a' + 10;
        else if (str[i] >= 'A' && str[i] <= 'F')
            value = str[i] - 'A' + 10;
        else
            break;

        result = result * str_base + value;
        i++;        
    }
    return (result * sign);
}