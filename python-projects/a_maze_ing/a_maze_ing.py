"""A-Maze-ing — Maze generator and visualizer.

Usage:
    python3 a_maze_ing.py config.txt

Reads a configuration file, generates a maze, writes it to a file
in hexadecimal wall encoding, and displays it interactively.
"""

import random
import sys

from maze.config import parse_config, validate_config, ConfigError
from maze.generator import Maze, MazeGenerator
from maze.pattern import (
    get_pattern_cells, place_pattern,
    PatternTooSmallError, PatternOverlapError,
)
from maze.solver import solve
from maze.renderer import render_maze, run_interactive
from maze.writer import write_maze


def _build_maze(
    config_width: int,
    config_height: int,
    config_entry: tuple[int, int],
    config_exit: tuple[int, int],
    seed: int | None,
    perfect: bool,
) -> tuple[Maze, str, list[tuple[int, int]]]:
    """Generate a maze, embed pattern, and solve.

    Args:
        config_width: Maze width.
        config_height: Maze height.
        config_entry: Entry coordinates.
        config_exit: Exit coordinates.
        seed: Random seed.
        perfect: Whether to generate a perfect maze.

    Returns:
        Tuple of (maze, path, pattern_cells).
    """
    pattern_cells: list[tuple[int, int]] = []
    try:
        pattern_cells = get_pattern_cells(
            config_width, config_height,
            config_entry, config_exit,
        )
    except (PatternTooSmallError, PatternOverlapError) as e:
        print(f"Warning: {e}")

    gen = MazeGenerator(
        config_width, config_height,
        config_entry, config_exit,
        seed=seed, perfect=perfect,
    )
    maze = gen.generate(blocked_cells=set(pattern_cells))

    if pattern_cells:
        place_pattern(maze, pattern_cells)

    path = solve(maze)
    return maze, path, pattern_cells


def main(config_path: str) -> None:
    """Run the maze generation pipeline.

    Args:
        config_path: Path to the configuration file.
    """
    # Parse and validate config
    raw = parse_config(config_path)
    config = validate_config(raw)

    # Build initial maze
    maze, path, pattern_cells = _build_maze(
        config.width, config.height,
        config.entry, config.exit,
        config.seed, config.perfect,
    )

    # Write output file
    write_maze(maze, path, config.output_file)
    print(f"Maze written to {config.output_file}")

    # Regenerate callback for interactive mode
    def regenerate() -> tuple[Maze, str, list[tuple[int, int]]]:
        new_seed = random.randint(0, 2**32)
        return _build_maze(
            config.width, config.height,
            config.entry, config.exit,
            new_seed, config.perfect,
        )

    # Launch interactive display
    try:
        run_interactive(
            maze, path, pattern_cells, regenerate,
        )
    except Exception:
        print(render_maze(
            maze, path=path,
            pattern_cells=pattern_cells,
        ))


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 a_maze_ing.py <config_file>")
        sys.exit(1)
    try:
        main(sys.argv[1])
    except ConfigError as e:
        print(f"Configuration error: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)
