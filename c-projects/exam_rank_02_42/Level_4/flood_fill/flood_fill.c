/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   flood_fill.c                                       :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2026/03/23 21:25:31 by omitrovs          #+#    #+#             */
/*   Updated: 2026/05/21 11:15:12 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */

#include <stdlib.h>
#include <unistd.h>

typedef struct  s_point
  {
    int           x;
    int           y;
  }               t_point;
  
void fill(char **tab, t_point size, t_point begin, char to_fill)
{
    if (begin.x < 0 || begin.x >= size.x || begin.y < 0 || begin.y >= size.y)
        return;


    if (tab[begin.y][begin.x] != to_fill)
        return;

    tab[begin.y][begin.x] = 'F';

    fill(tab, size, (t_point){begin.x - 1, begin.y}, to_fill);
    fill(tab, size, (t_point){begin.x + 1, begin.y}, to_fill);
    fill(tab, size, (t_point){begin.x, begin.y - 1}, to_fill);
    fill(tab, size, (t_point){begin.x, begin.y + 1}, to_fill);
    
}

void  flood_fill(char **tab, t_point size, t_point begin)
{
    char to_fill = tab[begin.y][begin.x];

    if (to_fill != 'F')
        fill(tab, size, begin, to_fill);
}