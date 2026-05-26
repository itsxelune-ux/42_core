#include <unistd.h>

int ft_atoi(char *str)
{
    int i = 0;
    int sign = 1;
    int result = 0;

    while (str[i] && ((str[i] >= 9 && str[i] <= 13) || str[i] == ' '))
        i++;
    
    if (str[i] == '+' || str[i] == '-')
    {
        if (str[i] == '-')
            sign = -1;
        i++;
    }

    while (str[i] && (str[i] >= '0' && str[i] <= '9'))
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }

    return (result * sign);
}

int print_hex(int c)
{
    char *hex = "0123456789abcdef";
    if (c > 16)
        print_hex(c / 16);

    write (1, &hex[c % 16], 1);
    return (0);
}

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int n = ft_atoi(av[1]);

    print_hex(n);

    return (write (1, "\n", 1), 0);
}