#include <unistd.h>
#include <stdio.h>

unsigned char   reverse_bits(unsigned char octet)
{
    int i = 8;
    int result;

    while (i-- > 0)
    {
        result = (result * 2) + (octet & 1);
        octet /= 2;
    }

    return (result);
}