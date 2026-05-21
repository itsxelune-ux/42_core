"""Output file writer for mazes.

Writes the maze to a file using hexadecimal wall encoding,
followed by entry/exit coordinates and the shortest path.
"""

from maze.generator import Maze


def write_maze(maze: Maze, path: str, filepath: str) -> None:
    """Write the maze to a file in hex format.

    Format:
        - One row per line, each cell encoded as a hex digit.
        - Empty line separator.
        - Entry coordinates (x,y).
        - Exit coordinates (x,y).
        - Shortest path as N/E/S/W string.
        - All lines end with newline.

    Args:
        maze: The generated Maze object.
        path: Shortest path string (e.g. 'EESSNNE').
        filepath: Output file path.

    Raises:
        OSError: If the file cannot be written.
    """
    try:
        with open(filepath, 'w') as f:
            for y in range(maze.height):
                row = ""
                for x in range(maze.width):
                    row += maze.get_cell(x, y).to_hex()
                f.write(row + "\n")
            f.write("\n")
            entry_x, entry_y = maze.entry
            exit_x, exit_y = maze.exit
            f.write(f"{entry_x},{entry_y}\n")
            f.write(f"{exit_x},{exit_y}\n")
            f.write(path + "\n")
    except OSError as e:
        raise OSError(
            f"Cannot write to '{filepath}': {e}"
        )
