/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   max.c                                              :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 11:03:54 by omitrovs          #+#    #+#             */
/*   Updated: 2026/05/21 11:02:05 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>

int max(int* tab, unsigned int len)
{
    unsigned int i = 1;
    int value = tab[0];

    while (i < len)
    {
        if (value < tab[i])
            value = tab[i];
        i++;
    }
    return (value);
}