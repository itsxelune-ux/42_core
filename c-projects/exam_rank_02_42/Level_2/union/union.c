// /* ************************************************************************** */
// /*                                                                            */
// /*                                                        :::      ::::::::   */
// /*   union.c                                            :+:      :+:    :+:   */
// /*                                                    +:+ +:+         +:+     */
// /*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
// /*                                                +#+#+#+#+#+   +#+           */
// /*   Created: 2026/03/24 06:10:02 by omitrovs          #+#    #+#             */
// /*   Updated: 2026/03/24 06:18:18 by omitrovs         ###   ########.fr       */
// /*                                                                            */
// /* ************************************************************************** */

#include <unistd.h>

int main(int ac, char **av)
{
    if (ac != 3)
        return (write (1, "\n", 1), 0);

    int i = 0;
    unsigned seen[256] = {0};

    char *str = av[1];
    while (str[i])
    {
        if (!seen[(unsigned char)str[i]])
        {
            write (1, &str[i], 1);
            seen[(unsigned char)str[i]] = 1;
        }
        i++;
    }

    i = 0;
    str = av[2];

    while (str[i])
    {
        if (!seen[(unsigned char)str[i]])
        {
            write (1, &str[i], 1);
            seen[(unsigned char)str[i]] = 1;
        }
        i++;
    }

    return (write (1, "\n", 1), 0);

}