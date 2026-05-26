#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int ft_len(int num)
{
    int count = 0;

    if (num <= 0)
        count++;

    while (num != 0)
    {
        num /= 10;
        count++;
    }
    return (count);
}

char    *ft_itoa(int nbr)
{
    int nb = nbr;
    int len = ft_len(nb);
   
    char *str = malloc (len + 1);
    if (!str)
        return (NULL);

    str[len] = '\0';

    if (nb < 0)
    {
        str[0] = '-';
        nb = -nb;
    }

    if (nb == 0)
        str[0] = '0';

    while (nb > 0)
    {
        str[len - 1] = (nb % 10) + '0';
        nb /= 10;
        len--;
    }
    return (str);
}


// int main(void)
// {
//     int number = -1234;
//     printf("%s", ft_itoa(number));
// }