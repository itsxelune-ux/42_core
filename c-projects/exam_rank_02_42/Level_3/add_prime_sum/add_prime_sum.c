#include <unistd.h>

void put_nbr(int num)
{
    if (num > 9)
        put_nbr(num / 10);

    char c = num % 10 + '0';
    write (1, &c, 1);
}

int ft_atoi(char *str)
{
    int i = 0;
    int result = 0;
    int sign = 1;

    while((str[i] >= 9 && str[i] <= 13) || str[i] == ' ')
        i++;

    if (str[i] == '+' || str[i] == '-')
    {
        if (str[i] == '-')
            sign = -1;
        i++;
    }

    while (str[i] >= '0' && str[i] <= '9')
    {
        result = result * 10 + (str[i] - '0');
        i++;
    }

    return (result * sign);
}

int prime_num(int num)
{
    if (num <= 1)
        return (0);

    int i = 2;

    while (i * i <= num)
    {
        if (num % i == 0)
            return (0);
        i++;
    }

    return (1);
}


int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "0\n", 2), 0);

    int num = ft_atoi(av[1]);
    int i = 0;
    int sum = 0;

    while (i <= num)
    {
        if (prime_num(i))
            sum = sum + i;
        i++;
    }

    put_nbr(sum);
    return (write (1, "\n", 1), 0);
}