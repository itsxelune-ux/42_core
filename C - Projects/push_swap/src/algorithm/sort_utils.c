/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   sort_utils.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/10 18:01:09 by omitrovs          #+#    #+#             */
/*   Updated: 2026/02/21 13:55:11 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*get_min_node(t_stack *stack)
{
	int		min_value;
	t_stack	*min_node;

	min_value = INT_MAX;
	min_node = NULL;
	if (!stack)
		return (NULL);
	while (stack)
	{
		if (stack->content < min_value)
		{
			min_value = stack->content;
			min_node = stack;
		}
		stack = stack->next;
	}
	return (min_node);
}

void	assign_index(t_stack *stack)
{
	int	i;
	int	median;

	i = 0;
	if (!stack)
		return ;
	median = ft_lstsize_ps(stack) / 2;
	while (stack)
	{
		stack->index = i;
		if (i <= median)
			stack->is_above_median = 1;
		else
			stack->is_above_median = 0;
		stack = stack->next;
		i++;
	}
}

void	fix_stack(t_stack **a)
{
	t_stack	*min_node;
	int		len;

	min_node = get_min_node(*a);
	len = ft_lstsize_ps(*a);
	while ((*a)->content != min_node->content)
	{
		if (min_node->index <= len / 2)
			ra(a);
		else
			rra(a);
	}
}

void	find_target_node(t_stack *a, t_stack *b)
{
	t_stack	*ptr_a;
	int		best_value;
	t_stack	*target;

	while (b)
	{
		target = NULL;
		best_value = INT_MAX;
		ptr_a = a;
		while (ptr_a)
		{
			if (ptr_a->content > b->content && ptr_a->content < best_value)
			{
				best_value = ptr_a->content;
				target = ptr_a;
			}
			ptr_a = ptr_a->next;
		}
		if (target == NULL)
			target = get_min_node(a);
		b->target_node = target;
		b = b->next;
	}
}

void	calculate_cost(t_stack *a, t_stack *b)
{
	int	len_a;
	int	len_b;

	len_a = ft_lstsize_ps(a);
	len_b = ft_lstsize_ps(b);
	while (b)
	{
		if (b->is_above_median)
			b->cost_b = b->index;
		else
			b->cost_b = (len_b - b->index) * (-1);
		if (b->target_node->is_above_median)
			b->cost_a = b->target_node->index;
		else
			b->cost_a = (len_a - b->target_node->index) * (-1);
		b = b->next;
	}
}
