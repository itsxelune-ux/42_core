#include <stdio.h>
#include <unistd.h>

size_t  ft_strcspn(const char *s, const char *reject)
{
    int i = 0;
    int j;

    while(s[i])
    {
        j = 0;
        while (reject[j])
        {
            if (s[i] == reject[j])
                return(i);
            j++;
        }
        i++;
    }

    return (i);

}


// int main(void)
// {
//     printf("%ld", ft_strcspn("lmao", "a"));
// }


