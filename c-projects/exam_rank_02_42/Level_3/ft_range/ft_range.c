/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 11:14:54 by omitrovs          #+#    #+#             */
/*   Updated: 2026/05/21 11:08:03 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

int     *ft_range(int start, int end)
{
    int i = 0;

    int len = abs(end - start) + 1;
    int *arr = malloc (sizeof(int) * len);

    if (start <= end)
    {
        while (start <= end)
        {
            arr[i++] = start++;
        }
    }
    else 
        while (start >= end)
        {
            arr[i++] = start--;
        }

    return (arr);
    
}

// int main(void)
// {
//     int start = 1;
//     int end = 3;
//     int len = abs(end - start) + 1;

//     int *arr = ft_range(start, end);
    
//     int i = 0;

//     while (i < len)
//     {
//         printf("%d", arr[i]);
//         i++;
//     }
//     return (0);
// }
