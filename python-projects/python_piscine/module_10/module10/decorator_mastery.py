from typing import Any
from collections.abc import Callable
from functools import wraps
import time


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args, **kwargs) -> Any:
        print(f"Casting {func.__name__}...")
        start_time = time.time()

        result = func(*args, **kwargs)

        end_time = time.time()
        print(f"Spell completed in {end_time - start_time:.3f} seconds")

        return result

    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            pwr = kwargs.get("power")

            if pwr is None and len(args) >= 3:
                pwr = args[2]

            if pwr is not None and pwr >= min_power:
                return func(*args, **kwargs)

            return "Insufficient power for this spell"

        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs) -> Any:
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)

                except Exception:
                    if attempt == max_attempts:
                        return f"Spell casting failed after {max_attempts} attempts"
                    else:
                        print(f"Spell failed, retrying... (attempt {attempt}/{max_attempts})")

        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    time.sleep(0.665)
    return "Fireball cast!"


@retry_spell(max_attempts=3)
def wrong_func() -> None:
    raise ValueError


@retry_spell(max_attempts=3)
def right_func() -> None:
    print("Waaaaaaagh spelled !")


def main() -> None:
    print("Testing spell timer...")
    print(f"Result: {fireball()}")
    print()

    print("Testing retrying spell...")
    wrong_func()
    right_func()

    print()

    print("Testing MageGuild...")
    mg = MageGuild()

    print(MageGuild.validate_mage_name("ilka"))
    print(MageGuild.validate_mage_name("      "))

    print(mg.cast_spell("Lightning", 15))
    print(mg.cast_spell("Lightning", -67))


if __name__ == "__main__":
    main()