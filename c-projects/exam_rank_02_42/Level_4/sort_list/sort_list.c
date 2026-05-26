#include <unistd.h>

typedef struct s_list t_list;

struct s_list {
    int data;
    t_list *next;
};

t_list  *sort_list(t_list* lst, int (*cmp)(int, int))
{
    t_list *cur = lst;
    int temp;
    while (cur && cur -> next)
    {
        if (!(cmp)(cur -> data, cur -> next -> data))
        {
            temp = cur -> data;
            cur -> data = cur -> next -> data;
            cur -> next -> data = temp;
            cur = lst;
        }
        else    
            cur = cur -> next;
    }
    return (lst);
}