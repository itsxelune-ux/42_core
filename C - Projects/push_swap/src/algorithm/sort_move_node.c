/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_move_node.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/11 17:07:17 by omitrovs          #+#    #+#             */
/*   Updated: 2026/02/14 18:28:31 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static t_stack	*get_cheapest_node(t_stack *b)
{
	int		cheapest_cost;
	t_stack	*target;
	t_stack	*b_ptr;

	b_ptr = b;
	cheapest_cost = INT_MAX;
	while (b_ptr)
	{
		if ((abs_v(b_ptr->cost_b) + abs_v(b_ptr->cost_a)) < cheapest_cost)
		{
			target = b_ptr;
			cheapest_cost = (abs_v(b_ptr->cost_b) + abs_v(b_ptr->cost_a));
		}
		b_ptr = b_ptr->next;
	}
	return (target);
}

void	move_cheapest_node(t_stack **a, t_stack **b)
{
	t_stack	*cheapest_node;

	cheapest_node = get_cheapest_node(*b);
	do_double_rotate(a, b, cheapest_node);
	do_single_rotate(a, b, cheapest_node);
	pa(a, b);
}
