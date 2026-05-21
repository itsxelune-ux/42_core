/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_tolower.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: ptison <ptison@student.42prague.com>       +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 17:24:43 by ptison            #+#    #+#             */
/*   Updated: 2025/11/12 17:28:05 by ptison           ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include "libft.h"
#include <stdio.h>

int	ft_tolower(int c)
{
	if (c >= 'A' && c <= 'Z')
		return (c + 32);
	return (c);
}
/*int main (void)
{
	char a = 'G';
	char lower = ft_tolower(a);

	printf("Before: '%c' -> ft_tolower: '%c'\n", a, lower);
	return (0);
}*/
