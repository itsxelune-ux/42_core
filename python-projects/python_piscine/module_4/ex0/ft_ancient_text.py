import sys


def ft_ancient_text() -> None:
    try:
        argc = len(sys.argv)
        if argc != 2:
            raise ValueError("Usage: ft_ancient_text.py <file>")
        print("=== Cyber Archives Recovery ===")

        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")

        f = open(filename, "r")
        content = f.read()
        print("---\n")
        print(content)
        print("\n---")
        print(f"File '{filename}' closed.")
        f.close()
    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    ft_ancient_text()
