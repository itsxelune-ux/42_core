/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_iterative_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 13:14:44 by ptison            #+#    #+#             */
/*   Updated: 2025/11/07 13:14:46 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <unistd.h>
#include <limits.h>

int	ft_iterative_factorial(int nb)
{
	int	result;

	result = 1;
	if (nb < 0)
		return (0);
	while (nb > 1)
	{
		if (result > INT_MAX / nb)
			return (0);
		result *= nb;
		nb--;
	}
	return (result);
}
/*int	main(void)
{
	printf("Factorial of 0: %d\n", ft_iterative_factorial(14));
	printf("Factorial of 1: %d\n", ft_iterative_factorial(1)); 
	printf("Factorial of 5: %d\n", ft_iterative_factorial(5));
	printf("Factorial of 10: %d\n", ft_iterative_factorial(10));
	printf("Factorial of -3: %d\n", ft_iterative_factorial(-3));
	return (0);
}*/
