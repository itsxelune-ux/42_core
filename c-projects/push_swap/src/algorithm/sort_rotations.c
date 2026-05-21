/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_rotations.c                                   :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 18:01:04 by omitrovs          #+#    #+#             */
/*   Updated: 2026/02/14 18:28:09 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

void	do_double_rotate(t_stack **a, t_stack **b, t_stack *cheapest_node)
{
	while (cheapest_node->cost_a > 0 && cheapest_node->cost_b > 0)
	{
		rr(a, b);
		cheapest_node->cost_a--;
		cheapest_node->cost_b--;
	}
	while (cheapest_node->cost_a < 0 && cheapest_node->cost_b < 0)
	{
		rrr(a, b);
		cheapest_node->cost_a++;
		cheapest_node->cost_b++;
	}
}

static void	do_a(t_stack **a, t_stack *cheapest_node)
{
	while (cheapest_node->cost_a)
	{
		if (cheapest_node->cost_a > 0)
		{
			ra(a);
			cheapest_node->cost_a--;
		}
		else if (cheapest_node->cost_a < 0)
		{
			rra(a);
			cheapest_node->cost_a++;
		}
	}
}

static void	do_b(t_stack **b, t_stack *cheapest_node)
{
	while (cheapest_node->cost_b)
	{
		if (cheapest_node->cost_b > 0)
		{
			rb(b);
			cheapest_node->cost_b--;
		}
		else if (cheapest_node->cost_b < 0)
		{
			rrb(b);
			cheapest_node->cost_b++;
		}
	}
}

void	do_single_rotate(t_stack **a, t_stack **b, t_stack *cheapest_node)
{
	do_a(a, cheapest_node);
	do_b(b, cheapest_node);
}
