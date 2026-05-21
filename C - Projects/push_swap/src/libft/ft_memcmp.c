/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_memcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 19:03:25 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 19:19:59 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stddef.h>
#include <stdio.h>

int	ft_memcmp(const void *s1, const void *s2, size_t n)
{
	size_t			i;
	unsigned char	*ptr1;
	unsigned char	*ptr2;

	ptr1 = (unsigned char *)s1;
	ptr2 = (unsigned char *)s2;
	i = 0;
	while (i < n)
	{
		if (ptr1[i] != ptr2[i])
			return (ptr1[i] - ptr2[i]);
		i++;
	}
	return (0);
}
/*int	main(void)
{
	const char	*a = "Helloo Ogi";
	const char	*b = "Helloo Ogi";
	const char	*c = "Hellpp Ogi";

	printf("Compare a vs b: %d\n", ft_memcmp(a, b, 10));
	printf("Compare a vs c: %d\n", ft_memcmp(a, c, 10));
	printf("Compare c vs a: %d\n", ft_memcmp(c, a, 10));

	return (0);
}*/
