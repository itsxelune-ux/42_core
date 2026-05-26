#include <unistd.h>

char *rev_print(char *str)
{

    int i = 0;

    while (str[i] != '\0')
        i++;

    i -= 1;

    while (i >= 0)
    {
        write (1, &str[i], 1);
        i--;
    }

    return (0);
}

// int main(void)
// {
//     rev_print("olgie");
//     rev_print("\n");
//     return (0);
// }
