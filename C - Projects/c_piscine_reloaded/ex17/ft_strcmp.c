/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_strcmp.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 14:02:40 by ptison            #+#    #+#             */
/*   Updated: 2025/11/07 14:02:42 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <string.h>

int	ft_strcmp(char *s1, char *s2)
{
	int	i;

	i = 0;
	while (s1[i] != '\0' && s1[i] == s2[i])
	{
		i++;
	}
	return (s1[i] - s2[i]);
}
/*int	main(void)
{
	char	s1[] = "Aello";
	char	s2[] = "Aelloo";
	int	result;

	printf("%d\n", strcmp(s1 ,s2));
	result = ft_strcmp(s1, s2);
	
	printf("%d\n",result);
	return (0);
}*/
