/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strncmp.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 18:56:43 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 18:57:29 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stddef.h>
#include <stdio.h>

int	ft_strncmp(const char *s1, const char *s2, size_t n)
{
	size_t	i;

	i = 0;
	while (i < n && (s1[i] || s2[i]))
	{
		if ((unsigned char)s1[i] != (unsigned char)s2[i])
			return ((unsigned char)s1[i] - (unsigned char)s2[i]);
		i++;
	}
	return (0);
}
/*int	main(void)
{
	int	result;

	result = ft_strncmp("Helloo Ogi", "Helloo Ogi", 10);
	printf("Compare same strings: %d\n", result);

	result = ft_strncmp("Helloo Ogi", "Hello Ogi", 10);
	printf("Compare different strings: %d\n", result);

	result = ft_strncmp("Helloo Ogi", "Hell", 4);
	printf("Compare first 4 characters: %d\n", result);

	result = ft_strncmp("Helloo Ogi", "Hellpp", 10);
	printf("Compare 'Helloo' vs 'Hellpp': %d\n", result);

	return (0);
}*/
