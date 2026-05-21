/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   push_swap.c                                        :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 18:54:24 by omitrovs          #+#    #+#             */
/*   Updated: 2026/02/14 18:29:32 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

static void	sort_handle(t_stack **a, t_stack **b)
{
	int	size;

	size = ft_lstsize_ps(*a);
	if (size == 2)
		sa(*a);
	else if (size == 3)
		sort_three(a);
	else
		sort(a, b);
	return ;
}

// void	print_stack(t_stack *stack)
// {
// 	t_stack *ptr;
// 	ptr = stack;
// 	while (ptr)
// 	{
// 		ft_printf("%i ", ptr->content);
// 		ptr = ptr->next;
// 	}
// }

int	main(int argc, char **argv)
{
	t_stack	*a;
	t_stack	*b;

	if (argc < 2)
		return (-1);
	a = NULL;
	b = NULL;
	parsing(argc, argv, &a);
	if (!is_sorted(a))
		sort_handle(&a, &b);
	free_stack(&a);
	if (b)
		free_stack(&b);
	return (0);
}
