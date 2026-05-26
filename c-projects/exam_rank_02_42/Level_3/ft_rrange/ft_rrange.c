#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int     *ft_rrange(int start, int end)
{
    int i =  0;
    int len = abs(end - start) + 1;
    int *arr = malloc(sizeof(int) * len);
    if (!arr)
        return (NULL);

    if (start <= end)
    {
        while (end >= start)
        {
            arr[i++] = end--;
        }
    }
    else    
        while (end <= start)
        {
            arr[i++] = end++;
        }

    return (arr);
}


// int main(void)
// {
//     int start = 0;
//     int end = -3;
//     int *arr = ft_rrange(start, end);
//     if (!arr)
//         return (0);

//     int len = abs(end - start) + 1;
//     int i = 0;

//     while (i < len)
//     {
//         printf("%d", arr[i]);
//         i++;
//     }

//     return (0);

// }