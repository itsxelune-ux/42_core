/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_printf.h                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/21 16:16:52 by omitrovs          #+#    #+#             */
/*   Updated: 2025/11/24 18:44:40 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#ifndef FT_PRINTF_H
# define FT_PRINTF_H

# include <stdarg.h>
# include <unistd.h>

int		ft_printf(const char *format, ...);
int		print_char(int c);
int		print_str(char *s);
int		print_nbr(long n);
int		print_unbr(unsigned int n);
int		print_hex(unsigned int n, int upper);
int		print_ptr(void *p);
int		print_hex_ul(unsigned long n);

#endif
