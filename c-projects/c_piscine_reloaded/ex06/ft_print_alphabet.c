/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_print_alphabet.c                                :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/06 18:37:48 by ptison            #+#    #+#             */
/*   Updated: 2025/11/10 15:17:38 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

/*void	ft_putchar(char c)
{
	write(1, &c, 1);
}*/
void	ft_putchar(char c);

void	ft_print_alphabet(void)
{
	char	a;

	a = 'a';
	while (a <= 'z')
	{
		ft_putchar(a);
		a++;
	}
}
/*int	main(void)
{
	ft_print_alphabet();
	return (0);
}*/
