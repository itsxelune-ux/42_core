/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_is_negative.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <marvin@42.fr>                    +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 18:55:00 by omitrovs          #+#    #+#             */
/*   Updated: 2025/11/06 18:55:05 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
/*
void   ft_putchar(char c)
{
    write(1, &c, 1);
}
*/
void	ft_putchar(char c);

void	ft_is_negative(int n)
{
	if (n < 0)
		ft_putchar('N');
	else
		ft_putchar('P');
}
// int main(void)
// {
// 	ft_is_negative(-5);
// 	write(1, "\n", 1);
// 	ft_is_negative(0);
// 	write(1, "\n", 1);
//     ft_is_negative(7);
//     write(1, "\n", 1);
// 	return 0;
// }
