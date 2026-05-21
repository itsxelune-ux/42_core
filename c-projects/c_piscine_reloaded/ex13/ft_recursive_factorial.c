/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_recursive_factorial.c                           :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 13:20:28 by ptison            #+#    #+#             */
/*   Updated: 2025/11/10 14:56:50 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <limits.h>
#include <stdio.h>

int	ft_recursive_factorial(int nb)
{
	int	sub;

	if (nb < 0)
		return (0);
	if (nb == 0 || nb == 1)
		return (1);
	sub = ft_recursive_factorial(nb - 1);
	if (sub == 0 || nb > INT_MAX / sub)
		return (0);
	return (nb * sub);
}

/*int	main(void)
{
	printf("Factorial of 5: %d\n", ft_recursive_factorial(5));   // 120
	printf("Factorial of 12: %d\n", ft_recursive_factorial(12)); // 479001600
	printf("Factorial of 13: %d\n", ft_recursive_factorial(13)); // 0 (overflow)
	return (0);
}*/
