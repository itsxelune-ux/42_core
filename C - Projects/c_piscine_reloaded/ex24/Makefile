# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Makefile                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2025/11/08 14:52:28 by ptison            #+#    #+#              #
#    Updated: 2025/11/08 19:47:12 by omitrovs         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

NAME = libft.a
SRC_PATH = ./srcs/
HEADER_PATH = ./includes/
FLAGS = -Wall -Wextra -Werror
INCLUDE = -I $(HEADER_PATH)

SRC = $(SRC_PATH)ft_putchar.c \
      $(SRC_PATH)ft_putstr.c \
      $(SRC_PATH)ft_strcmp.c \
      $(SRC_PATH)ft_strlen.c \
      $(SRC_PATH)ft_swap.c

OBJ = $(SRC:.c=.o)

all: $(NAME)

$(NAME): $(OBJ)
	ar rc $(NAME) $(OBJ)

%.o: $(SRC_PATH)%.c
	gcc $(FLAGS) $(INCLUDE) -c $< -o $@

clean:
	rm -f $(OBJ)

fclean: clean
	rm -f $(NAME)

re: fclean all

