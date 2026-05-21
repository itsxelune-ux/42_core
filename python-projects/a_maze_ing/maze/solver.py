"""Shortest path solver for mazes.

Uses BFS to guarantee the shortest path between entry and exit.
"""

from collections import deque
from maze.generator import Maze

DIRECTIONS: list[tuple[str, str, int, int]] = [
    ("N", "north", 0, -1),
    ("E", "east", 1, 0),
    ("S", "south", 0, 1),
    ("W", "west", -1, 0),
]


def solve(maze: Maze) -> str:
    """Find the shortest path from entry to exit using BFS.

    Only moves through open walls. Returns the path as a string
    of direction letters.

    Args:
        maze: A generated Maze object.

    Returns:
        A string of directions (e.g. 'EESSNNE'), each character
        being one of 'N', 'E', 'S', 'W'.

    Raises:
        ValueError: If no path exists between entry and exit.
    """
    visited: set[tuple[int, int]] = set()
    parent: dict[tuple[int, int], tuple[int, int, str]] = {}
    queue: deque[tuple[int, int]] = deque([maze.entry])
    visited.add(maze.entry)

    while queue:
        x, y = queue.popleft()
        if (x, y) == maze.exit:
            break
        cell = maze.get_cell(x, y)
        for letter, wall_name, offset_x, offset_y in DIRECTIONS:
            neighbor_x = x + offset_x
            neighbor_y = y + offset_y
            if (not getattr(cell, wall_name)
                    and 0 <= neighbor_x < maze.width
                    and 0 <= neighbor_y < maze.height
                    and (neighbor_x, neighbor_y)
                    not in visited):
                visited.add((neighbor_x, neighbor_y))
                parent[(neighbor_x, neighbor_y)] = (
                    x, y, letter
                )
                queue.append((neighbor_x, neighbor_y))

    if maze.exit not in parent and maze.entry != maze.exit:
        raise ValueError(
            "No path exists between entry and exit."
        )

    # Walk backwards from exit to entry
    path: list[str] = []
    current = maze.exit
    while current != maze.entry:
        if current not in parent:
            raise ValueError(
                "Path reconstruction failed: "
                f"cell {current} has no parent."
            )
        prev_x, prev_y, direction = parent[current]
        path.append(direction)
        current = (prev_x, prev_y)

    path.reverse()
    return "".join(path)
