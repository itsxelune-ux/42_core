#include <unistd.h>

int main(int ac, char **av)
{
    if (ac != 3)
        return (write (1, "\n",1 ), 0);

    int i = 0;
    int j;

    unsigned seen[256] = {0};

    while (av[1][i])
    {
        j = 0;
        while (av[2][j])
        {   
            if (av[1][i] == av[2][j])
            {
                if (!seen[(unsigned char) av[1][i]])
                {
                    write (1, &av[1][i], 1);
                    seen[(unsigned char)av[1][i]] = 1;
                }
                break;
            }
            j++;
        }
        i++;
    }

    return (write (1, "\n", 1), 0);
}