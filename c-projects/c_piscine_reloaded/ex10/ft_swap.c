/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_swap.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 13:03:27 by ptison            #+#    #+#             */
/*   Updated: 2025/11/07 13:03:30 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>

void	ft_swap(int *a, int *b)
{
	int	temp;

	temp = *a;
	*a = *b;
	*b = temp;
}
/*int main(void)
{
    int a;
    int b;

    a = 5;
    b = 10;
    printf("Before swap: a = %d, b = %d\n", a, b);
    ft_swap(&a, &b);
    printf("After swap: a = %d, b = %d", a, b);
    return (0);
}*/
