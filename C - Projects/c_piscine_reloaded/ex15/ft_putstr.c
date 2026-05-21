/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_putstr.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/07 13:25:20 by ptison            #+#    #+#             */
/*   Updated: 2025/11/07 13:25:22 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <stdio.h>
#include <unistd.h>

// void    ft_putchar(char c)
// {
//     write(1, &c, 1);
// }
void	ft_putchar(char c);

void	ft_putstr(char *str)
{
	while (*str)
	{
		ft_putchar(*str);
		str++;
	}
}
/*int main(void)
{
    char *smt;

    smt = "abcd";
    ft_putstr(smt);
    return (0);
}*/
