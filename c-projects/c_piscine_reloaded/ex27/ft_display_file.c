/* ************************************************************************** */
/*                                                                            */
/*                                                        :::      ::::::::   */
/*   ft_display_file.c                                  :+:      :+:    :+:   */
/*                                                    +:+ +:+         +:+     */
/*   By: omitrovs <omitrovs@student.42.fr>          +#+  +:+       +#+        */
/*                                                +#+#+#+#+#+   +#+           */
/*   Created: 2025/11/10 17:00:33 by ptison            #+#    #+#             */
/*   Updated: 2025/11/10 17:10:41 by omitrovs         ###   ########.fr       */
/*                                                                            */
/* ************************************************************************** */
#include <unistd.h>
#include <fcntl.h>

void	ft_puterror(char *msg)
{
	int	i;

	i = 0;
	while (msg[i])
	{
		write(2, &msg[i], 1);
		i++;
	}
}

void	ft_display_file(char *filename)
{
	int		fd;
	char	buf[1024];
	int		n;

	fd = open(filename, O_RDONLY);
	if (fd == -1)
	{
		ft_puterror("Cannot read file.\n");
		return ;
	}
	n = read(fd, buf, 1024);
	while (n > 0)
	{
		write(1, buf, n);
		n = read(fd, buf, 1024);
	}
	close(fd);
}

int	main(int argc, char **argv)
{
	if (argc < 2)
	{
		write(2, "File name missing.\n", 19);
		return (1);
	}
	else if (argc > 2)
	{
		write(2, "Too many arguments.\n", 20);
		return (1);
	}
	ft_display_file(argv[1]);
	return (0);
}
