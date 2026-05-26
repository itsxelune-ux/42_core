#include <stdio.h>
#include <unistd.h>

void put_nbr(int num)
{
    if (num > 9)
        put_nbr(num / 10);

    char c = (num % 10) + '0';
    write (1, &c, 1);
}

int main(int ac, char **av)
{
    (void)av;
    put_nbr(ac - 1);
    return (write(1, "\n", 1), 0);
}