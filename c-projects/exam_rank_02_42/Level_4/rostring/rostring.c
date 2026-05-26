// /* ************************************************************************** */
// /*                                                                            */
// /*                                                        :::      ::::::::   */
// /*   rostring.c                                         :+:      :+:    :+:   */
// /*                                                    +:+ +:+         +:+     */
// /*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
// /*                                                +#+#+#+#+#+   +#+           */
// /*   Created: 2026/03/24 06:26:41 by omitrovs          #+#    #+#             */
// /*   Updated: 2026/03/24 12:20:56 by omitrovs         ###   ########.fr       */
// /*                                                                            */
// /* ************************************************************************** */

#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>

int main(int ac, char **av)
{
	if (ac < 2)
		return (write (1, "\n", 1), 0);

	int i = 0;
	char *str = av[1];
	int first = 1;

	while (str[i] && (str[i] == '\t' || str[i] == ' '))
		i++;

	int start = i;

	while (str[i] && (str[i] != '\t' && str[i] != ' '))
		i++;

	int end = i;

	while (str[i])
	{
		while ((str[i] && str[i] == '\t') || str[i] == ' ')
			i++;

		if (str[i])
		{
			if (!first)
				write (1, " ", 1);
			first = 0;
		}
		
		while (((str[i] && str[i] != '\t') && str[i] != ' '))
		{
			write (1, &str[i], 1);
			i++;
		}
	}

	if (!first)
		write (1, " ", 1);

	while (start < end)
	{
		write (1, &str[start], 1);
		start++;
	}
	return (write (1, "\n", 1), 0);
}