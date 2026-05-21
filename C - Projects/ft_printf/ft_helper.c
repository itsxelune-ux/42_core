/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_helper.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/21 16:12:44 by omitrovs          #+#    #+#             */
/*   Updated: 2025/11/21 16:44:41 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdarg.h>
#include "ft_printf.h"

int	print_char(int c)
{
	write(1, &c, 1);
	return (1);
}

int	print_str(char *s)
{
	char	*str;
	int		i;

	if (s == NULL)
		str = "(null)";
	else
		str = s;
	i = 0;
	while (str[i])
	{
		write(1, &str[i], 1);
		i++;
	}
	return (i);
}

int	print_nbr(long n)
{
	int	count;

	count = 0;
	if (n < 0)
	{
		count += print_char('-');
		n = -n;
	}
	if (n >= 10)
		count += print_nbr(n / 10);
	count += print_char((n % 10) + '0');
	return (count);
}

int	print_unbr(unsigned int n)
{
	int	count;

	count = 0;
	if (n >= 10)
		count += print_unbr(n / 10);
	count += print_char((n % 10) + '0');
	return (count);
}

int	print_hex(unsigned int n, int upper)
{
	int		count;
	char	*base;

	count = 0;
	if (upper == 1)
		base = "0123456789ABCDEF";
	else
		base = "0123456789abcdef";
	if (n >= 16)
		count += print_hex(n / 16, upper);
	count += print_char(base[n % 16]);
	return (count);
}
