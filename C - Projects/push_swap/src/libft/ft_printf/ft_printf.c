/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/21 16:01:43 by omitrovs          #+#    #+#             */
/*   Updated: 2025/11/29 21:37:58 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <unistd.h>
#include <stdarg.h>
#include "ft_printf.h"

int	print_hex_ul(unsigned long n)
{
	char	*base;
	int		count;

	base = "0123456789abcdef";
	count = 0;
	if (n >= 16)
		count += print_hex_ul(n / 16);
	count += print_char(base[n % 16]);
	return (count);
}

int	print_ptr(void *p)
{
	unsigned long	addr;
	int				count;

	if (p == NULL)
		return (write(1, "(nil)", 5));
	addr = (unsigned long)p;
	write(1, "0x", 2);
	count = 2;
	count += print_hex_ul(addr);
	return (count);
}

static int	print_specifier(va_list ap, char c)
{
	if (c == 'c')
		return (print_char(va_arg(ap, int)));
	if (c == 's')
		return (print_str(va_arg(ap, char *)));
	if (c == 'd' || c == 'i')
		return (print_nbr(va_arg(ap, int)));
	if (c == 'u')
		return (print_unbr(va_arg(ap, unsigned int)));
	if (c == 'x')
		return (print_hex(va_arg(ap, unsigned int), 0));
	if (c == 'X')
		return (print_hex(va_arg(ap, unsigned int), 1));
	if (c == 'p')
		return (print_ptr(va_arg(ap, void *)));
	if (c == '%')
		return (print_char('%'));
	return (0);
}

int	ft_printf(const char *format, ...)
{
	va_list	ap;
	int		i;
	int		count;

	va_start(ap, format);
	i = 0;
	count = 0;
	while (format[i])
	{
		if (format[i] == '%')
		{
			i++;
			if (format[i])
				count += print_specifier(ap, format[i]);
			else
				break ;
		}
		else
			count += print_char(format[i]);
		i++;
	}
	va_end(ap);
	return (count);
}
