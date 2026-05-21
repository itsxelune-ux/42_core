"""Embedding of the '42' pattern into mazes.

Defines digit shapes as cell coordinate templates and handles
placement, wall closure, and size validation.
"""

from maze.generator import Maze


class PatternTooSmallError(Exception):
    """Raised when the maze is too small to fit the '42' pattern."""


class PatternOverlapError(Exception):
    """Raised when the '42' pattern overlaps entry or exit."""


# Relative (dx, dy) offsets for the '4' digit shape (3x5).
PATTERN_4: list[tuple[int, int]] = [
    (0, 0), (0, 1),
    (0, 2), (1, 2), (2, 2),
    (2, 3), (2, 4),
]

# Relative (dx, dy) offsets for the '2' digit shape (3x5).
PATTERN_2: list[tuple[int, int]] = [
    (0, 0), (1, 0), (2, 0),
    (2, 1),
    (0, 2), (1, 2), (2, 2),
    (0, 3),
    (0, 4), (1, 4), (2, 4),
]

PATTERN_WIDTH: int = 7
PATTERN_HEIGHT: int = 5


def can_fit_42(maze: Maze) -> bool:
    """Check if the maze is large enough to fit the '42' pattern.

    Args:
        maze: The Maze object to check.

    Returns:
        True if the pattern fits, False otherwise.
    """
    return (maze.width >= PATTERN_WIDTH + 2
            and maze.height >= PATTERN_HEIGHT + 2)


def get_pattern_cells(
    width: int,
    height: int,
    entry: tuple[int, int],
    exit: tuple[int, int],
) -> list[tuple[int, int]]:
    """Compute the '42' pattern cell positions without modifying the maze.

    Args:
        width: Maze width.
        height: Maze height.
        entry: Entry coordinates.
        exit: Exit coordinates.

    Returns:
        List of (x, y) coordinates of pattern cells.

    Raises:
        PatternTooSmallError: If the maze is too small.
        PatternOverlapError: If the pattern overlaps entry/exit.
    """
    if width < PATTERN_WIDTH + 2 or height < PATTERN_HEIGHT + 2:
        raise PatternTooSmallError(
            f"Maze too small ({width}x{height}) to embed "
            f"'42' pattern. Requires at least "
            f"{PATTERN_WIDTH + 2}x{PATTERN_HEIGHT + 2}."
        )

    # Center the pattern in the maze
    origin_x = (width - PATTERN_WIDTH) // 2
    origin_y = (height - PATTERN_HEIGHT) // 2

    # Build absolute coordinates for both digits
    pattern_cells: list[tuple[int, int]] = []
    for offset_x, offset_y in PATTERN_4:
        pattern_cells.append((origin_x + offset_x, origin_y + offset_y))
    # "2" is offset by 4 (3 wide + 1 gap)
    for offset_x, offset_y in PATTERN_2:
        pattern_cells.append((origin_x + 4 + offset_x,
                              origin_y + offset_y))

    # Check no pattern cell overlaps entry or exit
    for cell_x, cell_y in pattern_cells:
        if (cell_x, cell_y) in (entry, exit):
            raise PatternOverlapError(
                f"'42' pattern cell ({cell_x},{cell_y}) overlaps "
                f"with entry or exit."
            )

    return pattern_cells


def place_pattern(maze: Maze, pattern_cells: list[tuple[int, int]]) -> None:
    """Close all walls on pattern cells in the maze.

    Args:
        maze: The Maze object to embed the pattern into.
        pattern_cells: List of (x, y) coordinates to wall off.
    """
    for cell_x, cell_y in pattern_cells:
        for direction in ["N", "E", "S", "W"]:
            maze.close_wall(cell_x, cell_y, direction)
