#include <unistd.h>

int ft_atoi(char *str)
{
    int i = 0;
    int result = 0;

    while (str[i])
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }
    return (result);
}

void ft_print_num(int n)
{
    if (n > 9)
        ft_print_num(n / 10);

    char c = (n % 10) + '0';
    write (1, &c, 1);
}

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int num = ft_atoi(av[1]);
    int i = 1;
    int sum = 0;

    while (i <= 9)
    {
        sum = i * num;
        ft_print_num(i);
        write (1, " x ", 3);
        ft_print_num(num);
        write (1, " = ", 3);
        ft_print_num(sum);
        write (1, "\n", 1);
        i++;
    }
    return (0);
}