#include <stdlib.h>

typedef struct      s_list
{
    struct s_list   *next;
    void            *data;
}                   t_list;

void ft_list_remove_if(t_list **begin_list, void *data_ref, int (*cmp)())
{
  t_list **ptr = begin_list;
  t_list *temp;

  if ((cmp)((*ptr) -> data, data_ref) == 0)
  {
    temp = (*ptr);
    (*ptr) = (*ptr) -> next;

    free(temp);
  }
  else
    ptr = &((*ptr) -> next);
}
