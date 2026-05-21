/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_atoi.c                                          :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 19:12:08 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 19:16:50 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdio.h>

int	ft_atoi(const char *str)
{
	int	res;
	int	negative;

	negative = 1;
	res = 0;
	while (*str && (*str == ' ' || (*str >= 9 && *str <= 13)))
		str++;
	if (*str == '-')
		negative = -1;
	if (*str == '-' || *str == '+')
		str++;
	while (*str && *str >= '0' && *str <= '9')
	{
		res = res * 10 + (*str - '0');
		str++;
	}
	return (res * negative);
}
/*int	main(void)
{
	printf("ft_atoi(\"42\") = %d\n", ft_atoi("42"));
	printf("ft_atoi(\"   -42\") = %d\n", ft_atoi("   -42"));
	printf("ft_atoi(\"+123abc\") = %d\n", ft_atoi("+123abc"));
	printf("ft_atoi(\"  0\") = %d\n", ft_atoi("  0"));
	printf("ft_atoi(\"-2147483648\") = %d\n", ft_atoi("-2147483648"));
	printf("ft_atoi(\"2147483647\") = %d\n", ft_atoi("2147483647"));
	printf("ft_atoi(\"  \t\n 56\") = %d\n", ft_atoi("  \t\n 56"));
	printf("ft_atoi(\"--123\") = %d\n", ft_atoi("--123"));
	printf("ft_atoi(\"\") = %d\n", ft_atoi(""));
	return (0);
}*/
