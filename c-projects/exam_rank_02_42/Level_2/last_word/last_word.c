/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   last_word.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/11 12:59:44 by omitrovs          #+#    #+#             */
/*   Updated: 2026/05/21 11:01:21 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>
#include <unistd.h>

int main(int ac, char **av)
{
    if (ac != 2)
        return (write (1, "\n", 1), 0);

    int i = 0;

    while(av[1][i])
        i++;
    i--;

    while (i >= 0 && ((av[1][i] >= 9 && av[1][i] <= 13) || av[1][i] == ' '))
        i--;
    

    int end = i;
    while (i >= 0 && (!(av[1][i] >= 9 && av[1][i] <= 13) && av[1][i] != ' '))
        i--;

    write (1, &av[1][i + 1], end - i);
    return (write (1, "\n", 1), 0);   
}