/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_range.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 15:19:18 by omitrovs          #+#    #+#             */
/*   Updated: 2025/11/07 15:19:29 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <stdlib.h>

int	*ft_range(int min, int max)
{
	int	*arr;
	int	size;	
	int	i;

	if (min >= max)
		return (NULL);
	size = max - min;
	arr = (int *)malloc(sizeof(int) * size);
	if (!arr)
		return (NULL);
	i = 0;
	while (i < size)
	{
		arr[i] = min + i;
		i++;
	}
	return (arr);
}
/*int	main(void)
{
	int	min;
	int	max;
	int	*range;
	int	i;

	min = 3;
	max = 10;
	range = ft_range(min, max);
	if (range == NULL)
	{
		printf("Returned NULL.\n");
		return (1);
	}
	i = 0;
	while (i < max - min)
	{
		printf("%d ", range[i]);
		i++;
	}
	printf("\n");
	free(range);
	return (0);
}*/
