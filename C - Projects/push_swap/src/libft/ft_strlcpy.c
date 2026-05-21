/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcpy.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 15:39:08 by ptison            #+#    #+#             */
/*   Updated: 2025/11/16 17:52:48 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

size_t	ft_strlcpy(char *dst, const char *src, size_t size)
{
	size_t	i;

	i = 0;
	if (size != 0)
	{
		while (src[i] && i < size - 1)
		{
			dst[i] = src[i];
			i++;
		}
		dst[i] = '\0';
	}
	while (src[i])
		i++;
	return (i);
}
/*int	main(void)
{
	char	src[] = "HelloWorld";
	char	dst[6];
	size_t	ret;

	ret = ft_strlcpy(dst, src, sizeof(dst));

	printf("Source: %s\n", src);
	printf("Destination: %s\n", dst);
	printf("Returned length: %zu\n", ret);

	return (0);
}*/
