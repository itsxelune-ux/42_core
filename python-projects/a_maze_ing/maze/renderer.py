"""Visual rendering of mazes.

Provides ASCII terminal rendering with optional path overlay,
'42' pattern highlighting, ANSI color support, and interactive
display using curses.
"""

import curses
from typing import Callable

from maze.generator import Maze

# ANSI escape codes
RESET = "\033[0m"

# Color schemes: wall, entry, exit, path, pattern
COLOR_SCHEMES: list[dict[str, str]] = [
    {  # 0: No colors
        "wall": "",
        "entry": "",
        "exit": "",
        "path": "",
        "pattern": "",
    },
    {  # 1: Classic
        "wall": "\033[37m",      # white
        "entry": "\033[32m",     # green
        "exit": "\033[31m",      # red
        "path": "\033[33m",      # yellow
        "pattern": "\033[35m",   # magenta
    },
    {  # 2: Ocean
        "wall": "\033[36m",      # cyan
        "entry": "\033[32m",     # green
        "exit": "\033[31m",      # red
        "path": "\033[34m",      # blue
        "pattern": "\033[35m",   # magenta
    },
    {  # 3: Forest
        "wall": "\033[32m",      # green
        "entry": "\033[33m",     # yellow
        "exit": "\033[31m",      # red
        "path": "\033[36m",      # cyan
        "pattern": "\033[35m",   # magenta
    },
]

# Direction offsets for walking the path
PATH_OFFSETS: dict[str, tuple[int, int]] = {
    "N": (0, -1),
    "E": (1, 0),
    "S": (0, 1),
    "W": (-1, 0),
}


def _get_path_cells(
    maze: Maze,
    path: str,
) -> set[tuple[int, int]]:
    """Convert a path string into a set of cell coordinates.

    Args:
        maze: The Maze object.
        path: Direction string (e.g. 'EESSNNE').

    Returns:
        Set of (x, y) coordinates on the path.
    """
    cells: set[tuple[int, int]] = set()
    x, y = maze.entry
    cells.add((x, y))
    for direction in path:
        offset_x, offset_y = PATH_OFFSETS[direction]
        x += offset_x
        y += offset_y
        cells.add((x, y))
    return cells


def render_maze(
    maze: Maze,
    path: str | None = None,
    pattern_cells: list[tuple[int, int]] | None = None,
    color_scheme: int = 0,
) -> str:
    """Render the maze as an ASCII string.

    Args:
        maze: The Maze object to render.
        path: Optional shortest path string to overlay.
        pattern_cells: Optional list of '42' pattern cell coords
            to highlight.
        color_scheme: Index of the color scheme to use (0-2).

    Returns:
        A multi-line string representing the maze.
    """
    path_cells: set[tuple[int, int]] = set()
    if path is not None:
        path_cells = _get_path_cells(maze, path)

    pattern_set: set[tuple[int, int]] = set()
    if pattern_cells is not None:
        pattern_set = set(pattern_cells)

    scheme = COLOR_SCHEMES[color_scheme % len(COLOR_SCHEMES)]
    c_wall = scheme["wall"]
    c_entry = scheme["entry"]
    c_exit = scheme["exit"]
    c_path = scheme["path"]
    c_pattern = scheme["pattern"]
    r = RESET if color_scheme != 0 else ""

    lines: list[str] = []

    for y in range(maze.height):
        # Top wall line
        top = ""
        for x in range(maze.width):
            cell = maze.get_cell(x, y)
            top += f"{c_wall}+{r}"
            top += f"{c_wall}---{r}" if cell.north else "   "
        top += f"{c_wall}+{r}"
        lines.append(top)

        # Cell content line
        mid = ""
        for x in range(maze.width):
            cell = maze.get_cell(x, y)
            if cell.west:
                mid += f"{c_wall}|{r}"
            else:
                mid += " "
            # Cell interior
            if (x, y) == maze.entry:
                mid += f"{c_entry} S {r}"
            elif (x, y) == maze.exit:
                mid += f"{c_exit} E {r}"
            elif (x, y) in pattern_set:
                mid += f"{c_pattern}###{r}"
            elif (x, y) in path_cells:
                mid += f"{c_path} * {r}"
            else:
                mid += "   "
        # Right border of last cell
        last_cell = maze.get_cell(maze.width - 1, y)
        if last_cell.east:
            mid += f"{c_wall}|{r}"
        else:
            mid += " "
        lines.append(mid)

    # Bottom wall line
    bottom = ""
    for x in range(maze.width):
        cell = maze.get_cell(x, maze.height - 1)
        bottom += f"{c_wall}+{r}"
        bottom += f"{c_wall}---{r}" if cell.south else "   "
    bottom += f"{c_wall}+{r}"
    lines.append(bottom)

    return "\n".join(lines)


def run_interactive(
    maze: Maze,
    path: str,
    pattern_cells: list[tuple[int, int]],
    regenerate: Callable[[], tuple[Maze, str, list[tuple[int, int]]]],
) -> None:
    """Launch the interactive curses display.

    Supports the following keys:
        R - Regenerate maze with a new seed.
        P - Toggle shortest path overlay.
        C - Cycle wall color scheme.
        Q - Quit.
        4 - Toggle '42' pattern highlight.

    Args:
        maze: The initial Maze object to display.
        path: The shortest path string.
        pattern_cells: List of '42' pattern cell coordinates.
        regenerate: Callable that returns (new_maze, new_path,
            new_pattern_cells) when called.
    """
    curses.wrapper(
        _interactive_loop, maze, path, pattern_cells, regenerate
    )


def _interactive_loop(
    stdscr: "curses.window",
    maze: Maze,
    path: str,
    pattern_cells: list[tuple[int, int]],
    regenerate: Callable[[], tuple[Maze, str, list[tuple[int, int]]]],
) -> None:
    """Main curses loop.

    Args:
        stdscr: The curses standard screen.
        maze: Current Maze object.
        path: Current shortest path string.
        pattern_cells: Current '42' pattern cell coordinates.
        regenerate: Callable to regenerate the maze.
    """
    show_path = False
    show_pattern = True
    color_scheme = 0

    while True:
        stdscr.clear()

        # Render maze to string (no ANSI colors in curses mode)
        display_path = path if show_path else None
        display_pattern = pattern_cells if show_pattern else None
        output = render_maze(
            maze, path=display_path,
            pattern_cells=display_pattern,
            color_scheme=0,
        )

        # Draw maze
        for row_idx, line in enumerate(output.split("\n")):
            try:
                stdscr.addstr(row_idx, 0, line)
            except curses.error:
                pass

        # Draw help bar
        help_y = maze.height * 2 + 2
        help_text = (
            "[R] Regenerate  [P] Toggle path  "
            "[C] Color  [4] Toggle 42  [Q] Quit"
        )
        scheme_names = ["No color", "Classic", "Ocean", "Forest"]
        status = (
            f"Path: {'ON' if show_path else 'OFF'}  "
            f"42: {'ON' if show_pattern else 'OFF'}  "
            f"Color: {scheme_names[color_scheme % len(scheme_names)]}"
        )
        try:
            stdscr.addstr(help_y, 0, help_text)
            stdscr.addstr(help_y + 1, 0, status)
        except curses.error:
            pass

        # Apply curses colors if scheme > 0
        if color_scheme > 0:
            _apply_curses_colors(stdscr, maze, color_scheme,
                                 show_path, path,
                                 show_pattern, pattern_cells)

        stdscr.refresh()

        # Wait for keypress
        key = stdscr.getch()
        if key in (ord('q'), ord('Q')):
            break
        elif key in (ord('r'), ord('R')):
            maze, path, pattern_cells = regenerate()
        elif key in (ord('p'), ord('P')):
            show_path = not show_path
        elif key in (ord('c'), ord('C')):
            color_scheme = (color_scheme + 1) % len(COLOR_SCHEMES)
        elif key == ord('4'):
            show_pattern = not show_pattern


def _apply_curses_colors(
    stdscr: "curses.window",
    maze: Maze,
    color_scheme: int,
    show_path: bool,
    path: str,
    show_pattern: bool,
    pattern_cells: list[tuple[int, int]],
) -> None:
    """Apply curses color pairs to the rendered maze.

    Args:
        stdscr: The curses standard screen.
        maze: Current Maze object.
        color_scheme: Current color scheme index.
        show_path: Whether path is displayed.
        path: Path string.
        show_pattern: Whether pattern is displayed.
        pattern_cells: Pattern cell coordinates.
    """
    # Initialize color pairs based on scheme
    curses.start_color()
    curses.use_default_colors()

    # Color pair mapping: 1=wall, 2=entry, 3=exit, 4=path, 5=pattern
    scheme_colors = [
        [],  # 0: no color
        [curses.COLOR_WHITE, curses.COLOR_GREEN,
         curses.COLOR_RED, curses.COLOR_YELLOW,
         curses.COLOR_MAGENTA],
        [curses.COLOR_CYAN, curses.COLOR_GREEN,
         curses.COLOR_RED, curses.COLOR_BLUE,
         curses.COLOR_MAGENTA],
        [curses.COLOR_GREEN, curses.COLOR_YELLOW,
         curses.COLOR_RED, curses.COLOR_CYAN,
         curses.COLOR_MAGENTA],
    ]

    idx = color_scheme % len(scheme_colors)
    if idx == 0:
        return
    colors = scheme_colors[idx]
    for i, color in enumerate(colors):
        curses.init_pair(i + 1, color, -1)

    path_cells: set[tuple[int, int]] = set()
    if show_path:
        path_cells = _get_path_cells(maze, path)
    pattern_set: set[tuple[int, int]] = set()
    if show_pattern and pattern_cells:
        pattern_set = set(pattern_cells)

    for y in range(maze.height):
        screen_y = y * 2 + 1  # cell content row
        for x in range(maze.width):
            screen_x = x * 4 + 1  # cell content col
            if (x, y) == maze.entry:
                try:
                    stdscr.addstr(screen_y, screen_x, " S ",
                                  curses.color_pair(2))
                except curses.error:
                    pass
            elif (x, y) == maze.exit:
                try:
                    stdscr.addstr(screen_y, screen_x, " E ",
                                  curses.color_pair(3))
                except curses.error:
                    pass
            elif (x, y) in pattern_set:
                try:
                    stdscr.addstr(screen_y, screen_x, "###",
                                  curses.color_pair(5))
                except curses.error:
                    pass
            elif (x, y) in path_cells:
                try:
                    stdscr.addstr(screen_y, screen_x, " * ",
                                  curses.color_pair(4))
                except curses.error:
                    pass
