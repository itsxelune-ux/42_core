/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_numbers.c                                 :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 18:48:57 by ptison            #+#    #+#             */
/*   Updated: 2025/11/06 18:48:59 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>

// void	ft_putchar(char c)
// {
// 	write(1, &c, 1);
// }
void	ft_putchar(char c);

void	ft_print_numbers(void)
{
	char	a;

	a = '0';
	while (a <= '9')
	{
		ft_putchar(a);
		a++;
	}
}

/*int main (void)
{
	ft_print_numbers();
	return 0;
}*/
