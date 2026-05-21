/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strdup.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 14:21:04 by ptison            #+#    #+#             */
/*   Updated: 2025/11/07 14:21:06 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdlib.h>
#include <unistd.h>
#include <stdio.h>

char	*ft_strdup(char *src)
{
	int			i;
	char		*dup;

	i = 0;
	while (src[i])
		i++;
	dup = (char *) malloc (sizeof (char) * (i + 1));
	if (dup == NULL)
		return (NULL);
	i = 0;
	while (src[i])
	{
		dup[i] = src[i];
		i++;
	}
	dup[i] = '\0';
	return (dup);
}
/*int main(void)
{
    char *original = "Hello, world!";
    char *copy = ft_strdup(original);

    if (copy == NULL)
    {
        printf("Memory allocation failed.\n");
        return 1;
    }

    printf("Original: %s\n", original);
    printf("Copy: %s\n", copy);

    free(copy);
    return 0;
}*/
