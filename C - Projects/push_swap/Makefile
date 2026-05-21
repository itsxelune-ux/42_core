# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/02/14 18:30:53 by omitrovs          #+#    #+#              #
#    Updated: 2026/02/21 14:06:30 by omitrovs         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME       = push_swap
CC         = cc
CFLAGS     = -Wall -Wextra -Werror

LIBFT_PATH = ./src/libft
LIBFT_NAME = $(LIBFT_PATH)/libft.a

SRCS       = src/operations/push.c \
             src/operations/reverse_rotate.c \
             src/operations/rotate.c \
             src/operations/swap.c \
             src/algorithm/sort_move_node.c \
             src/algorithm/sort_rotations.c \
             src/algorithm/sort_small.c \
             src/algorithm/sort_utils.c \
             src/algorithm/sort.c \
             src/stack/list.c \
             src/parsing/parsing.c \
             src/utils/utils.c \
             src/push_swap.c

OBJS       = $(SRCS:src/%.c=objects/%.o)

INCLUDES   = -Iinclude -I$(LIBFT_PATH)

all: $(LIBFT_NAME) $(NAME)

$(LIBFT_NAME):
	@$(MAKE) -C $(LIBFT_PATH)

$(NAME): $(OBJS) $(LIBFT_NAME)
	$(CC) $(CFLAGS) $(OBJS) -L$(LIBFT_PATH) -lft -o $(NAME)

objects/%.o: src/%.c
	@mkdir -p $(dir $@)
	$(CC) $(CFLAGS) $(INCLUDES) -c $< -o $@

clean:
	rm -rf objects
	@$(MAKE) -C $(LIBFT_PATH) clean

fclean: clean
	rm -f $(NAME)
	@$(MAKE) -C $(LIBFT_PATH) fclean

re: fclean all

.PHONY: all clean fclean re
