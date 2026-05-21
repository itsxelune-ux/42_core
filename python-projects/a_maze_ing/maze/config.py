"""Configuration file parser and validator."""

from dataclasses import dataclass
import random


class ConfigError(Exception):
    """Base class for configuration errors."""


class ConfigFileNotFound(ConfigError):
    """Raised when the config file cannot be found."""


class ConfigSyntaxError(ConfigError):
    """Raised when a line has invalid syntax."""


class ConfigMissingKeys(ConfigError):
    """Raised when required keys are missing."""


class ConfigValueError(ConfigError):
    """Raised when a config value is invalid."""


@dataclass
class MazeConfig:
    """Validated maze configuration.

    Attributes:
        width: Maze width in cells.
        height: Maze height in cells.
        entry: Entry coordinates (x, y).
        exit: Exit coordinates (x, y).
        output_file: Path to write the output maze file.
        perfect: Whether to generate a perfect maze.
        seed: Random seed for reproducibility.
    """

    width: int
    height: int
    entry: tuple[int, int]
    exit: tuple[int, int]
    output_file: str
    perfect: bool
    seed: int | None = None


def parse_config(filepath: str) -> dict[str, str]:
    """Parse config file into a dict of key-value pairs.

    Args:
        filepath: Path to the configuration file.

    Returns:
        Dictionary of string keys to string values.

    Raises:
        ConfigFileNotFound: If the file does not exist.
        ConfigSyntaxError: If a line has invalid syntax.
    """
    if not filepath.endswith(".txt"):
        raise ConfigSyntaxError(
            f"Configuration file '{filepath}' "
            "must be a .txt file"
        )
    config: dict[str, str] = {}
    try:
        with open(filepath, "r") as file:
            for linenum, line in enumerate(file, start=1):
                line = line.strip()
                if not line or line.startswith("#"):
                    continue
                if "=" not in line:
                    raise ConfigSyntaxError(
                        "Invalid syntax on line "
                        f"{linenum}: '{line}'"
                    )
                key, value = line.split("=", 1)
                config[key.strip().upper()] = value.strip()
    except FileNotFoundError:
        raise ConfigFileNotFound(
            f"Configuration file '{filepath}' "
            "not found"
        )
    except UnicodeDecodeError:
        raise ConfigSyntaxError(
            f"Configuration file '{filepath}' "
            "is not a valid text file"
        )
    return config


def _is_on_border(
    x: int, y: int, width: int, height: int,
) -> bool:
    """Check if coordinates are on the maze border.

    Args:
        x: Horizontal position.
        y: Vertical position.
        width: Maze width.
        height: Maze height.

    Returns:
        True if the cell is on the border.
    """
    return (
        x == 0 or x == width - 1
        or y == 0 or y == height - 1
    )


def validate_config(raw: dict[str, str]) -> MazeConfig:
    """Validate config values and return a MazeConfig.

    Args:
        raw: Raw key-value dict from parse_config.

    Returns:
        A validated MazeConfig object.

    Raises:
        ConfigMissingKeys: If required keys are missing.
        ConfigValueError: If any value is invalid.
    """
    required = {
        "WIDTH", "HEIGHT", "ENTRY",
        "EXIT", "OUTPUT_FILE", "PERFECT",
    }
    missing = required - raw.keys()
    if missing:
        raise ConfigMissingKeys(
            "Missing required configuration keys: "
            f"{', '.join(sorted(missing))}"
        )

    # WIDTH and HEIGHT
    try:
        width = int(raw["WIDTH"])
        if width <= 0:
            raise ConfigValueError(
                "WIDTH must be a positive integer > 0"
            )
    except ValueError:
        raise ConfigValueError(
            f"WIDTH value invalid: {raw['WIDTH']}"
            " (must be a positive integer)"
        )

    try:
        height = int(raw["HEIGHT"])
        if height <= 0:
            raise ConfigValueError(
                "HEIGHT must be a positive integer > 0"
            )
    except ValueError:
        raise ConfigValueError(
            f"HEIGHT value invalid: {raw['HEIGHT']}"
            " (must be a positive integer)"
        )

    if width == 1 and height == 1:
        raise ConfigValueError(
            "Maze must have at least 2 cells "
            "(1x1 is not allowed)"
        )

    # ENTRY and EXIT
    try:
        entry = tuple(
            int(x.strip())
            for x in raw["ENTRY"].split(",")
        )
        exit_ = tuple(
            int(x.strip())
            for x in raw["EXIT"].split(",")
        )
    except Exception:
        raise ConfigValueError(
            "ENTRY and EXIT must be in format x,y "
            "with integers"
        )

    if len(entry) != 2 or len(exit_) != 2:
        raise ConfigValueError(
            "ENTRY and EXIT must have exactly "
            "2 coordinates (x,y)"
        )

    for name, coord in [("ENTRY", entry), ("EXIT", exit_)]:
        x, y = coord
        if x < 0 or x >= width or y < 0 or y >= height:
            raise ConfigValueError(
                f"{name} coordinates {coord} are out "
                f"of bounds for a "
                f"{width}x{height} maze"
            )

    if entry == exit_:
        raise ConfigValueError(
            "Cannot create maze: "
            "ENTRY and EXIT must be different cells"
        )

    for name, coord in [("ENTRY", entry), ("EXIT", exit_)]:
        if not _is_on_border(
            coord[0], coord[1], width, height
        ):
            raise ConfigValueError(
                f"{name} must be on the maze border"
            )

    # OUTPUT_FILE
    output_file = raw["OUTPUT_FILE"]
    if not output_file.strip():
        raise ConfigValueError(
            "OUTPUT_FILE must be a non-empty string"
        )

    # PERFECT
    perfect_str = raw["PERFECT"].lower()
    if perfect_str not in {"true", "false"}:
        raise ConfigValueError(
            "PERFECT must be True or False "
            "(case-insensitive)"
        )
    perfect = perfect_str == "true"

    # Optional SEED
    seed: int | None = None
    if "SEED" in raw:
        try:
            seed = int(raw["SEED"])
        except ValueError:
            raise ConfigValueError(
                "SEED must be an integer, "
                f"got: {raw['SEED']}"
            )
    else:
        seed = random.randint(0, 2**32 - 1)
        print(
            f"No SEED provided. Using seed: {seed}"
        )

    return MazeConfig(
        width=width,
        height=height,
        entry=entry,
        exit=exit_,
        output_file=output_file,
        perfect=perfect,
        seed=seed,
    )
