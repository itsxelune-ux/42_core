/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_sqrt.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 13:22:52 by ptison            #+#    #+#             */
/*   Updated: 2025/11/07 13:22:54 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

int	ft_sqrt(int nb)
{
	int	i;

	i = 1;
	if (nb <= 0)
		return (0);
	while (i <= nb / i)
	{
		if (i * i == nb)
			return (i);
		i++;
	}
	return (0);
}
/*int	main(void)
{
	printf("Num: %d\n", ft_sqrt(0));
	printf("Num: %d\n", ft_sqrt(16));
	printf("Num: %d\n", ft_sqrt(-16));
	printf("Num: %d\n", ft_sqrt(81));
	return (0);
}*/
