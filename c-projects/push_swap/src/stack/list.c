/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   list.c                                             :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/02/06 20:02:24 by omitrovs          #+#    #+#             */
/*   Updated: 2026/02/14 18:18:08 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include "push_swap.h"

t_stack	*ft_lstnew_ps(int content)
{
	t_stack	*res;

	res = (t_stack *)malloc(sizeof(t_stack));
	if (!res)
		return (NULL);
	res->content = content;
	res->index = -1;
	res->is_above_median = -1;
	res->next = NULL;
	return (res);
}

void	ft_lstadd_front_ps(t_stack **lst, t_stack *new)
{
	if (!lst || !new)
		return ;
	new->next = *lst;
	*lst = new;
}

int	ft_lstsize_ps(t_stack *lst)
{
	int	size;

	if (!lst)
		return (0);
	size = 1;
	while (lst->next)
	{
		size++;
		lst = lst->next;
	}
	return (size);
}

t_stack	*ft_lstlast_ps(t_stack *lst)
{
	if (!lst)
		return (NULL);
	while (lst->next)
		lst = lst->next;
	return (lst);
}

void	ft_lstadd_back_ps(t_stack **lst, t_stack *new)
{
	t_stack	*last_node;

	if (!lst || !new)
		return ;
	if (*lst == NULL)
		*lst = new;
	else
	{
		last_node = ft_lstlast_ps(*lst);
		last_node->next = new;
	}
}
