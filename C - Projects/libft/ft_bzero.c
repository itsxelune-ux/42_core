/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_bzero.c                                         :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/12 14:46:29 by ptison            #+#    #+#             */
/*   Updated: 2025/11/16 17:48:57 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "libft.h"

void	ft_bzero(void *s, size_t n)
{
	ft_memset(s, 0, n);
}
/*
int	main(void)
{
	int	i = 0;
	int	*s = NULL;
	int	n = 5;
	ft_bzero(s, 3);
	while (i < n)
	{
		printf("%i ", s[i]);
		i++;
	}
}
*/