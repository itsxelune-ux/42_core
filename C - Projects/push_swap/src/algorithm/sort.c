/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 17:07:25 by omitrovs          #+#    #+#             */
/*   Updated: 2026/02/17 15:16:39 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static int	get_pivot(t_stack *a, int size)
{
	int	sum;

	sum = 0;
	while (a)
	{
		sum += a->content;
		a = a->next;
	}
	return (sum / size);
}

static void	sort_b(t_stack **a, t_stack **b)
{
	while (*b)
	{
		assign_index(*a);
		assign_index(*b);
		find_target_node(*a, *b);
		calculate_cost(*a, *b);
		move_cheapest_node(a, b);
	}
}

void	sort(t_stack **a, t_stack **b)
{
	int	size;
	int	size_init;
	int	pivot;

	size = ft_lstsize_ps(*a);
	size_init = size;
	pivot = get_pivot(*a, size);
	while (size > 3)
	{
		pb(a, b);
		if ((*b)->content < pivot && size_init != 5)
			if ((*b)->next)
				rb(b);
		size--;
	}
	sort_three(a);
	sort_b(a, b);
	assign_index(*a);
	fix_stack(a);
}
