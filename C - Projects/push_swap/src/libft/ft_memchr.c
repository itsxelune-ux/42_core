/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memchr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 19:00:25 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 19:00:43 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stddef.h>
#include <stdio.h>

void	*ft_memchr(const void *s, int c, size_t n)
{
	size_t			i;
	unsigned char	*ptr;

	ptr = (unsigned char *)s;
	i = 0;
	while (i < n)
	{
		if (ptr[i] == (unsigned char)c)
			return (&ptr[i]);
		i++;
	}
	return (NULL);
}
/*int	main(void)
{
	const char	*str = "Helloo Ogi";
	void		*ptr;

	ptr = ft_memchr(str, 'o', 10);
	if (ptr)
		printf("First 'o' found at index: %ld\n", (char *)ptr - str);
	else
		printf("'o' not found\n");

	ptr = ft_memchr(str, 'z', 10);
	if (ptr)
		printf("First 'z' found at index: %ld\n", (char *)ptr - str);
	else
		printf("'z' not found\n");

	ptr = ft_memchr(str, '\0', 11);
	if (ptr)
		printf("Null terminator found at index: %ld\n", (char *)ptr - str);

	return (0);
}*/
