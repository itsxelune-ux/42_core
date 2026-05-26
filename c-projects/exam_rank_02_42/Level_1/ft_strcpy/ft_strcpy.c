#include <unistd.h>

char    *ft_strcpy(char *s1, char *s2)
{
    int i = 0;

    while (s2[i])
    {
        s1[i] = s2[i];
        i++;
    }

    s1[i] = '\0';

    return (s1);
}

int main(void)
{
    char s1[100];
    char s2[] = "hello";

    ft_strcpy(s1, s2);

    write(1, s1, 5);

    return (0);
}