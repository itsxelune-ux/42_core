// /* ************************************************************************** */
// /*                                                                            */
// /*                                                        :::      ::::::::   */
// /*   ft_strdup.c                                        :+:      :+:    :+:   */
// /*                                                    +:+ +:+         +:+     */
// /*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
// /*                                                +#+#+#+#+#+   +#+           */
// /*   Created: 2026/03/21 21:59:27 by omitrovs          #+#    #+#             */
// /*   Updated: 2026/05/10 15:46:30 by omitrovs         ###   ########.fr       */
// /*                                                                            */
// /* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

char    *ft_strdup(char *src)
{
    char *dst;
    int len = 0;


    while (src[len])
        len++;
    dst = malloc (sizeof(char) * len + 1);

    if (!dst)
        return NULL;

    int i = 0;

    while (src[i])
    {
        dst[i] = src[i];
        i++;
    }

    dst[i] = '\0';

    return (dst);

}


// int main(void)
// {
//     char *str = "hello";
//     char *result = ft_strdup(str);
//     printf("%s", result);
// }