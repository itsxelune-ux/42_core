/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 17:33:29 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 17:34:20 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stddef.h>
#include <stdio.h>

char	*ft_strchr(const char *s, int c)
{
	while (*s)
	{
		if (*s == (char)c)
			return ((char *)s);
		s++;
	}
	if (c == '\0')
		return ((char *)s);
	return (NULL);
}
/*int	main(void)
{
	const char	*str = "Hello, Norminette!";
	char		*ptr;

	ptr = ft_strchr(str, 'o');
	if (ptr)
		printf("'o' found at index: %ld\n", ptr - str);
	else
		printf("'o' not found\n");

	ptr = ft_strchr(str, 'z');
	if (ptr)
		printf("'z' found at index: %ld\n", ptr - str);
	else
		printf("'z' not found\n");

	ptr = ft_strchr(str, '\0');
	printf("Null terminator at index: %ld\n", ptr - str);

	return (0);
}*/
