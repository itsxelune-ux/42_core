*This project has been created as part of the 42 curriculum by mmacku, omitrovs*

## Description

A-Maze-ing is a maze generator written in Python 3.10+. It reads a configuration file, generates a random maze (optionally perfect), embeds a visible "42" pattern, finds the shortest path, writes the maze to a file in hexadecimal wall encoding, and provides an interactive terminal display.

## Instructions

### Installation

```bash
python3 -m venv venv
source venv/bin/activate
make install
```

### Running

```bash
make run
# or
python3 a_maze_ing.py config.txt
```

### Debug Mode

```bash
make debug
```

### Linting

```bash
make lint
```

### Testing

```bash
make test
```

### Building the Package

```bash
pip install build
python3 -m build
```

### Clean

```bash
make clean
```

## Configuration File Format

The configuration file uses `KEY=VALUE` pairs, one per line. Lines starting with `#` are comments.

| Key | Required | Type | Description | Example |
|-----|----------|------|-------------|---------|
| `WIDTH` | Yes | int > 0 | Maze width in cells | `WIDTH=20` |
| `HEIGHT` | Yes | int > 0 | Maze height in cells | `HEIGHT=15` |
| `ENTRY` | Yes | x,y | Entry coordinates | `ENTRY=0,0` |
| `EXIT` | Yes | x,y | Exit coordinates | `EXIT=19,14` |
| `OUTPUT_FILE` | Yes | string | Output file path | `OUTPUT_FILE=maze.txt` |
| `PERFECT` | Yes | bool | Perfect maze (one path) | `PERFECT=True` |
| `SEED` | No | int | Random seed for reproducibility | `SEED=42` |

Example config file:

```
# Maze configuration
WIDTH=20
HEIGHT=15
ENTRY=0,0
EXIT=19,14
OUTPUT_FILE=maze.txt
PERFECT=True
SEED=42
```

## Maze Generation Algorithm

### Recursive Backtracker (DFS)

We chose the Recursive Backtracker algorithm for maze generation. It works by:

1. Starting at the entry cell, marking it as visited.
2. Randomly choosing an unvisited neighbor, opening the wall between them, and moving there.
3. When no unvisited neighbors exist, backtracking to the previous cell.
4. Repeating until all cells are visited.

**Why this algorithm:**

- Naturally produces perfect mazes (exactly one path between any two cells) without additional processing.
- Simple to implement and understand.
- Produces mazes with long, winding corridors that look visually interesting.
- Well-documented and widely used in maze generation.

### Non-Perfect Mode

When `PERFECT=False`, the generator first creates a perfect maze, then randomly removes ~20% of internal walls to create loops (alternative paths). Each removal is checked against a 3x3 open area constraint to ensure corridors never exceed 2 cells in width.

### Pathfinding

BFS (Breadth-First Search) is used to find the shortest path from entry to exit. BFS guarantees the shortest path in an unweighted graph, which is exactly what a maze is.

## Reusable Module

The maze generator is packaged as `mazegen-1.0.0` and can be installed via pip:

```bash
pip install mazegen-1.0.0-py3-none-any.whl
```

### Usage Example

```python
from maze import MazeGenerator
from maze.solver import solve

# Create and generate a maze
gen = MazeGenerator(
    width=20, height=15,
    entry=(0, 0), exit=(19, 14),
    seed=42, perfect=True,
)
maze = gen.generate()

# Find the shortest path
path = solve(maze)
print(f"Shortest path: {path}")

# Access the maze structure
for y in range(maze.height):
    for x in range(maze.width):
        cell = maze.get_cell(x, y)
        print(f"({x},{y}): N={cell.north} E={cell.east} "
              f"S={cell.south} W={cell.west}")
```

### Parameters

- `width`, `height`: Maze dimensions in cells.
- `entry`, `exit`: Tuple coordinates `(x, y)`.
- `seed`: Integer for reproducibility. `None` for random.
- `perfect`: `True` for a single-path maze, `False` for loops.

### Accessing the Structure

- `maze.get_cell(x, y)` returns a `Cell` with boolean walls: `.north`, `.east`, `.south`, `.west`.
- `cell.to_hex()` returns the hexadecimal wall encoding.
- `solve(maze)` returns the shortest path as a string of `N`, `E`, `S`, `W`.

## Interactive Display

The program launches a terminal-based interactive display (curses). Controls:

| Key | Action |
|-----|--------|
| `R` | Regenerate maze with a new random seed |
| `P` | Toggle shortest path overlay |
| `C` | Cycle wall color scheme |
| `4` | Toggle "42" pattern highlight |
| `Q` | Quit |

Color schemes: No color, Classic, Ocean, Forest.

## Team and Project Management

### Roles

- **Person A (Core Engine):** Maze data structures, generation algorithm, "42" pattern, pathfinding, main integration, API design.
- **Person B (Interface Layer):** Project setup, config parsing, hex output, ASCII rendering, user interaction, packaging, documentation.

### Planning

The project was split into 8 phases across 70 tasks. The initial plan allowed both team members to work in parallel from day one, with only light dependencies between the two workstreams.

### What Worked Well

- The parallel split between engine and interface minimized blocking.
- Defining the data model early (Cell, Maze classes) gave both team members a stable API to code against.
- Writing tests alongside implementation caught bugs early.

### What Could Be Improved

- Earlier integration testing between Person A and Person B code would have caught API mismatches sooner.
- The "42" pattern placement needed to be integrated into the generation step (not post-generation), which required a redesign mid-project.

### Tools Used

- Python 3.10+, flake8, mypy, pytest
- curses (stdlib) for terminal UI
- setuptools + build for packaging
- Git for version control

## Resources

- [Maze Generation Algorithms (Wikipedia)](https://en.wikipedia.org/wiki/Maze_generation_algorithm)
- [Recursive Backtracker](https://en.wikipedia.org/wiki/Maze_generation_algorithm#Randomized_depth-first_search)
- [BFS Shortest Path](https://en.wikipedia.org/wiki/Breadth-first_search)
- [Python curses documentation](https://docs.python.org/3/library/curses.html)
- [PEP 257 - Docstring Conventions](https://peps.python.org/pep-0257/)

### AI Usage

AI (Claude) was used as a development assistant for:
- Planning the project structure and task breakdown.
- Debugging wall consistency and pattern placement issues.
- Fixing lint and type-checking errors.
- Writing documentation.

