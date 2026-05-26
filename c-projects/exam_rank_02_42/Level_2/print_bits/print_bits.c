#include <unistd.h>

void    print_bits(unsigned char octet)
{
    int bit;
    char str[8];
    int i = 8;

    while (i-- > 0)
    {
        bit = (octet & 1) + '0';
        octet /= 2;
        str[i] = bit;

    }

    write (1, str, 8);
}