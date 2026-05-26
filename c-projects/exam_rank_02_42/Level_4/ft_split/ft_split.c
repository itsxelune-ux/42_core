/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_split.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 11:50:56 by omitrovs          #+#    #+#             */
/*   Updated: 2026/05/21 11:19:45 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <stdlib.h>

char **ft_split(char *str)
{
    int i = 0;
    int j = 0;
    int count = 0;

    while (str[i])
    {
        if (str[i] != ' ' && str[i] != '\t' && str[i] != '\n')
        {
            if (i == 0 ||
                str[i - 1] == ' ' ||
                str[i - 1] == '\t' ||
                str[i - 1] == '\n')
                count++;
        }
        i++;
    }
    char **arr = malloc(sizeof(char *) * (count + 1));
    i = 0;

    while (str[i])
    {
        while (str[i] == ' ' || str[i] == '\t' || str[i] == '\n')
            i++;

        if (!str[i])
            break;

        int start = i;

        while (str[i] &&
               str[i] != ' ' &&
               str[i] != '\t' &&
               str[i] != '\n')
            i++;

        int len = i - start;

        arr[j] = malloc(len + 1);

        int k = 0;
        while (k < len)
        {
            arr[j][k] = str[start + k];
            k++;
        }
        arr[j][k] = '\0';
        j++;
    }
    arr[j] = NULL;
    return arr;
}