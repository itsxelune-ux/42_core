"""Maze data model and generation logic.

Contains the Cell and Maze data structures, and the MazeGenerator
class that implements maze generation algorithms.
"""

from dataclasses import dataclass
import random


@dataclass
class Cell:
    """A single cell in the maze grid.

    Each cell has a position (x, y) and four walls (north, east, south, west).
    All walls start closed (True).

    Attributes:
        x: Horizontal position in the grid (column).
        y: Vertical position in the grid (row).
        north: Whether the north wall is closed.
        east: Whether the east wall is closed.
        south: Whether the south wall is closed.
        west: Whether the west wall is closed.
    """

    x: int
    y: int
    north: bool = True
    east: bool = True
    south: bool = True
    west: bool = True

    def to_hex(self) -> str:
        """Convert wall state to a hex character.

        Bit encoding: 0=North, 1=East, 2=South, 3=West.
        A closed wall sets the bit to 1.

        Returns:
            A single uppercase hex character ('0'-'F').
        """
        value: int = 0
        if self.north:
            value += 1
        if self.east:
            value += 2
        if self.south:
            value += 4
        if self.west:
            value += 8
        return format(value, 'X')


class Maze:
    """A 2D grid of cells representing the maze.

    Attributes:
        width: Number of cells horizontally.
        height: Number of cells vertically.
        entry: Entry cell coordinates (x, y).
        exit: Exit cell coordinates (x, y).
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
    ) -> None:
        """Initialize a maze with all walls closed.

        Args:
            width: Number of cells horizontally.
            height: Number of cells vertically.
            entry: Entry cell coordinates (x, y).
            exit: Exit cell coordinates (x, y).
        """
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self._grid: list[list[Cell]] = [
            [Cell(x, y) for x in range(width)]
            for y in range(height)
        ]

    def get_cell(self, x: int, y: int) -> Cell:
        """Get the cell at position (x, y).

        Args:
            x: Horizontal position (column).
            y: Vertical position (row).

        Returns:
            The Cell at the given position.

        Raises:
            IndexError: If coordinates are out of bounds.
        """
        if x < 0 or x >= self.width:
            raise IndexError(
                f"x={x} out of bounds "
                f"(0-{self.width - 1})"
            )
        if y < 0 or y >= self.height:
            raise IndexError(
                f"y={y} out of bounds "
                f"(0-{self.height - 1})"
            )
        return self._grid[y][x]

    def open_wall(self, x: int, y: int, direction: str) -> None:
        """Open a wall on a cell and the corresponding neighbor wall.

        Ensures wall consistency between adjacent cells.

        Args:
            x: Cell horizontal position.
            y: Cell vertical position.
            direction: One of 'N', 'E', 'S', 'W'.
        """
        cell = self.get_cell(x, y)
        match direction:
            case "N":
                cell.north = False
                if y - 1 >= 0:
                    self.get_cell(x, y - 1).south = False
            case "E":
                cell.east = False
                if x + 1 < self.width:
                    self.get_cell(x + 1, y).west = False
            case "S":
                cell.south = False
                if y + 1 < self.height:
                    self.get_cell(x, y + 1).north = False
            case "W":
                cell.west = False
                if x - 1 >= 0:
                    self.get_cell(x - 1, y).east = False

    def close_wall(self, x: int, y: int, direction: str) -> None:
        """Close a wall on a cell and the corresponding neighbor wall.

        Ensures wall consistency between adjacent cells.

        Args:
            x: Cell horizontal position.
            y: Cell vertical position.
            direction: One of 'N', 'E', 'S', 'W'.
        """
        cell = self.get_cell(x, y)
        match direction:
            case "N":
                cell.north = True
                if y - 1 >= 0:
                    self.get_cell(x, y - 1).south = True
            case "E":
                cell.east = True
                if x + 1 < self.width:
                    self.get_cell(x + 1, y).west = True
            case "S":
                cell.south = True
                if y + 1 < self.height:
                    self.get_cell(x, y + 1).north = True
            case "W":
                cell.west = True
                if x - 1 >= 0:
                    self.get_cell(x - 1, y).east = True

    def enforce_borders(self) -> None:
        """Close all walls on the outer edges of the maze."""
        for x in range(self.width):
            self.get_cell(x, 0).north = True
            self.get_cell(x, self.height - 1).south = True
        for y in range(self.height):
            self.get_cell(0, y).west = True
            self.get_cell(self.width - 1, y).east = True


class MazeGenerator:
    """Generates mazes using configurable algorithms.

    Attributes:
        width: Maze width in cells.
        height: Maze height in cells.
        entry: Entry coordinates (x, y).
        exit: Exit coordinates (x, y).
        seed: Random seed for reproducibility.
        perfect: Whether to generate a perfect maze (single path).
        maze: The generated Maze object (None until generate() is called).
    """

    def __init__(
        self,
        width: int,
        height: int,
        entry: tuple[int, int],
        exit: tuple[int, int],
        seed: int | None = None,
        perfect: bool = True,
    ) -> None:
        """Initialize the generator with maze parameters.

        Args:
            width: Maze width in cells.
            height: Maze height in cells.
            entry: Entry coordinates (x, y).
            exit: Exit coordinates (x, y).
            seed: Random seed. If None, a random seed is chosen.
            perfect: If True, generate a perfect maze.
        """
        self.width = width
        self.height = height
        self.entry = entry
        self.exit = exit
        self.seed = seed
        self.perfect = perfect
        self._maze: Maze | None = None

    def generate(
        self,
        blocked_cells: set[tuple[int, int]] | None = None,
    ) -> Maze:
        """Generate the maze and return it.

        Args:
            blocked_cells: Optional set of cells to treat as walls
                (e.g. '42' pattern cells). These cells will not be
                visited during generation.

        Returns:
            The generated Maze object.
        """
        if self.seed is None:
            self.seed = random.randint(0, 2**32)
        random.seed(self.seed)
        self._maze = Maze(self.width, self.height, self.entry, self.exit)
        blocked: set[tuple[int, int]] = blocked_cells or set()
        visited: set[tuple[int, int]] = set(blocked)
        stack: list[tuple[int, int]] = []
        start: tuple[int, int] = self.entry
        visited.add(start)
        stack.append(start)

        while stack:
            current = stack[-1]
            cx, cy = current
            neighbors: list[tuple[int, int, str]] = []
            if cy - 1 >= 0 and (cx, cy - 1) not in visited:
                neighbors.append((cx, cy - 1, "N"))
            if cx + 1 < self.width and (cx + 1, cy) not in visited:
                neighbors.append((cx + 1, cy, "E"))
            if cy + 1 < self.height and (cx, cy + 1) not in visited:
                neighbors.append((cx, cy + 1, "S"))
            if cx - 1 >= 0 and (cx - 1, cy) not in visited:
                neighbors.append((cx - 1, cy, "W"))
            if neighbors:
                nx, ny, direction = random.choice(neighbors)
                self._maze.open_wall(cx, cy, direction)
                visited.add((nx, ny))
                stack.append((nx, ny))
            else:
                stack.pop()

        self._maze.enforce_borders()
        for px, py in [self.entry, self.exit]:
            if px == 0:
                self._maze.open_wall(px, py, "W")
            elif px == self.width - 1:
                self._maze.open_wall(px, py, "E")
            elif py == 0:
                self._maze.open_wall(px, py, "N")
            elif py == self.height - 1:
                self._maze.open_wall(px, py, "S")

        if not self.perfect:
            self._remove_walls()

        return self._maze

    def _remove_walls(self) -> None:
        """Remove random internal walls to create loops.

        Collects all closed internal walls, shuffles them,
        and removes a percentage to make a non-perfect maze.
        """
        if self._maze is None:
            raise RuntimeError("Maze not generated yet")
        walls: list[tuple[int, int, str]] = []
        for y in range(self.height):
            for x in range(self.width):
                cell = self._maze.get_cell(x, y)
                # Only collect East and South to avoid duplicates
                if x + 1 < self.width and cell.east:
                    walls.append((x, y, "E"))
                if y + 1 < self.height and cell.south:
                    walls.append((x, y, "S"))

        random.shuffle(walls)
        to_remove = len(walls) // 5  # remove ~20%
        removed = 0
        for wall_x, wall_y, direction in walls:
            if removed >= to_remove:
                break
            self._maze.open_wall(wall_x, wall_y, direction)
            if self._has_3x3_open(wall_x, wall_y):
                self._maze.close_wall(wall_x, wall_y, direction)
            else:
                removed += 1

    def _has_3x3_open(self, x: int, y: int) -> bool:
        """Check if any 3x3 block overlapping (x, y) is fully open.

        Args:
            x: Cell x coordinate.
            y: Cell y coordinate.

        Returns:
            True if a 3x3 open area exists.
        """
        if self._maze is None:
            raise RuntimeError("Maze not generated yet")
        for block_y in range(max(0, y - 2), min(self.height - 2, y + 1)):
            for block_x in range(max(0, x - 2), min(self.width - 2, x + 1)):
                if self._is_block_open(block_x, block_y):
                    return True
        return False

    def _is_block_open(self, block_x: int, block_y: int) -> bool:
        """Check if the 3x3 block starting at (block_x, block_y) is fully open.

        Args:
            block_x: Top-left x of the block.
            block_y: Top-left y of the block.

        Returns:
            True if all internal walls in the block are open.
        """
        if self._maze is None:
            raise RuntimeError("Maze not generated yet")
        for offset_y in range(3):
            for offset_x in range(3):
                cell = self._maze.get_cell(
                    block_x + offset_x, block_y + offset_y
                )
                if offset_x < 2 and cell.east:
                    return False
                if offset_y < 2 and cell.south:
                    return False
        return True

    def validate(
        self,
        blocked_cells: set[tuple[int, int]] | None = None,
    ) -> bool:
        """Validate maze connectivity and constraints.

        Runs BFS from entry to check all non-blocked cells are
        reachable through open walls.

        Args:
            blocked_cells: Optional set of cells to exclude from
                the reachability check (e.g. '42' pattern cells).

        Returns:
            True if the maze is valid.
        """
        if self._maze is None:
            return False
        from collections import deque
        blocked: set[tuple[int, int]] = blocked_cells or set()
        directions = [
            ("north", 0, -1),
            ("east", 1, 0),
            ("south", 0, 1),
            ("west", -1, 0),
        ]
        visited: set[tuple[int, int]] = set(blocked)
        queue: deque[tuple[int, int]] = deque([self.entry])
        visited.add(self.entry)

        while queue:
            x, y = queue.popleft()
            cell = self._maze.get_cell(x, y)
            for wall_name, offset_x, offset_y in directions:
                neighbor_x = x + offset_x
                neighbor_y = y + offset_y
                if (not getattr(cell, wall_name)
                        and 0 <= neighbor_x < self.width
                        and 0 <= neighbor_y < self.height
                        and (neighbor_x, neighbor_y) not in visited):
                    visited.add((neighbor_x, neighbor_y))
                    queue.append((neighbor_x, neighbor_y))

        return len(visited) == self.width * self.height
