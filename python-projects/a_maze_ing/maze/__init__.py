"""maze — A maze generation and solving package.

Provides tools for generating random mazes, embedding patterns,
finding shortest paths, and rendering mazes visually.

Example:
    from maze import MazeGenerator

    gen = MazeGenerator(width=20, height=15, entry=(0, 0),
                        exit=(19, 14), seed=42, perfect=True)
    maze = gen.generate()
"""

from maze.generator import Cell, Maze, MazeGenerator

__all__ = ["Cell", "Maze", "MazeGenerator"]
