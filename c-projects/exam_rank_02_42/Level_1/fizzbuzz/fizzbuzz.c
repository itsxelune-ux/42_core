#include <unistd.h>

void put_nbr(int n)
{
    if (n > 9)
        put_nbr(n / 10);

    char c = n % 10 + '0'; 
    write (1, &c, 1);

}

int main(void)
{

    int num = 1;
    while (num <= 100)
    {
        if ((num % 3 == 0) && (num % 5 == 0))
            write (1, "fizzbuzz", 8);
        else if (num % 3 == 0)
            write (1, "fizz", 4);
        else if (num % 5 == 0)
            write (1, "buzz", 4);
        else 
            put_nbr(num);
        write (1, "\n", 1);
        num++;
    }

    return (0);
}