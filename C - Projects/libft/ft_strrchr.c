/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strrchr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 18:51:20 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 18:53:38 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stddef.h>
#include <stdio.h>

char	*ft_strrchr(const char *s, int c)
{
	int	i;

	i = 0;
	while (s[i])
		i++;
	while (i >= 0)
	{
		if (s[i] == (char)c)
			return ((char *)&s[i]);
		i--;
	}
	return (NULL);
}
/*int	main(void)
{
	const char	*str = "Helloo Ogi";
	char		*ptr;

	ptr = ft_strrchr(str, 'o');
	if (ptr)
		printf("Last 'o' found at index: %ld\n", ptr - str);
	else
		printf("'o' not found\n");

	ptr = ft_strrchr(str, 'H');
	if (ptr)
		printf("Last 'H' found at index: %ld\n", ptr - str);
	else
		printf("'H' not found\n");

	ptr = ft_strrchr(str, '\0');
	printf("Null terminator found at index: %ld\n", ptr - str);

	return (0);
}*/
