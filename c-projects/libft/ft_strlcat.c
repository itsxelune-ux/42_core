/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strlcat.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 15:42:17 by ptison            #+#    #+#             */
/*   Updated: 2025/11/16 17:57:43 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

size_t	ft_strlcat(char *dst, const char *src, size_t size)
{
	size_t	i;
	size_t	dst_len;
	size_t	src_len;

	src_len = 0;
	while (src[src_len])
		src_len++;
	if (dst == NULL && size == 0)
		return (src_len);
	dst_len = 0;
	while (dst[dst_len] && dst_len < size)
		dst_len++;
	if (dst_len == size)
		return (size + src_len);
	i = 0;
	while (src[i] && dst_len + i < size - 1)
	{
		dst[dst_len + i] = src[i];
		i++;
	}
	if (size > 0)
		dst[dst_len + i] = '\0';
	return (dst_len + src_len);
}
/*int	main(void)
{
	char	dst[12] = "Hello";
	char	src[] = "World";
	size_t	ret;

	ret = ft_strlcat(dst, src, sizeof(dst));

	printf("After strlcat:\n");
	printf("Destination: %s\n", dst);
	printf("Returned length: %zu\n", ret);

	return (0);
}*/
