/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_list_size.c                                     :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/24 06:19:12 by omitrovs          #+#    #+#             */
/*   Updated: 2026/05/21 11:07:37 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>

typedef struct    s_list
{
    struct s_list *next;
    void          *data;
}                 t_list;


int     ft_list_size(t_list *begin_list)
{
    int len;

    while(begin_list)
    {
        begin_list = begin_list -> next;
        len++;
    }
    return (len);
}