/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strnstr.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 19:08:33 by ptison            #+#    #+#             */
/*   Updated: 2025/11/16 17:59:39 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

char	*ft_strnstr(const char *haystack, const char *needle, size_t len)
{
	size_t	i;
	size_t	j;

	if (haystack == NULL && len == 0)
		return (NULL);
	if (needle[0] == '\0')
		return ((char *)haystack);
	i = 0;
	while (haystack[i] != '\0' && i < len)
	{
		j = 0;
		while (haystack[i + j] != '\0'
			&& needle[j] != '\0'
			&& (i + j) < len
			&& haystack[i + j] == needle[j])
			j++;
		if (needle[j] == '\0')
			return ((char *)&haystack[i]);
		i++;
	}
	return (NULL);
}
/*int	main(void)
{
	const char	*str = "Helloo Ogi";
	char		*res;

	res = ft_strnstr(str, "Ogi", 11);
	if (res)
		printf("'Ogi' found at index: %ld\n", res - str);
	else
		printf("'Ogi' not found\n");

	res = ft_strnstr(str, "Ogi", 5);
	if (res)
		printf("'Ogi' found within first 5 chars\n");
	else
		printf("'Ogi' not found within first 5 chars\n");

	res = ft_strnstr(str, "", 11);
	if (res)
		printf("Empty string returns start of haystack\n");

	return (0);
}*/
