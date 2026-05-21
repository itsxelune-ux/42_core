from typing import Optional, Tuple


def secure_archive(filename: str,
                   action: Optional[str],
                   content: Optional[str]) -> Tuple[bool, str]:
    try:
        if action == 'r':
            with open(filename, 'r') as f:
                return (True, f.read())
        elif action == 'w':
            with open(filename, 'w') as f:
                f.write(content if content is not None else "")
            return (True, "Content successfully written to file")
        else:
            return (False, "Invalid action")
    except PermissionError as e:
        return (False, str(e))
    except FileNotFoundError as e:
        return (False, str(e))


def main() -> None:
    print("=== Cyber Archives Security ===\n")
    text = "hello\nworld\n!"

    print("Using 'secure_archive' to read from a nonexistent file:")
    print(secure_archive("/not/existing/file", 'r', text))

    print("\nUsing 'secure_archive' to read from an inaccessible file:")
    print(secure_archive("/etc/master.passwd", 'r', text))

    print("\nUsing 'secure_archive' to read from a regular file")
    content = secure_archive("test.txt", 'r', text)
    print(content)

    print("\nUsing 'secure_archive' to write previous content to a new file:")
    print(secure_archive("output.txt", 'w', content[1]))


if __name__ == "__main__":
    main()
