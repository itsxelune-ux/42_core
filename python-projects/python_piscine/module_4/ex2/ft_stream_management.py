import sys


def ft_stream_management() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        argc = len(sys.argv)
        if argc != 2:
            raise ValueError("Usage: python3 ft_ancient_text.py <filename>")
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        f = open(filename, "r")
        string = f.read()
        print(f"---\n\n{string}\n\n---")
        arr = string.split('\n')
        print(f"File '{filename}' closed.")
        f.close()

        print("\nTransform data:")
        new_arr = []
        new_arr = [s + "#" for s in arr]
        print("---\n")
        for s in new_arr:
            print(s)
        print("\n---")
        print("Enter new file name (or empty): ", end="", flush=True)

        newfilename = sys.stdin.readline().strip()

        if not newfilename:
            print("Data not saved.")
            return
        print(f"Saving data to '{newfilename}'")
        f = open(newfilename, "w")
        for i in range(0, len(new_arr) - 1, 1):
            f.write(new_arr[i] + "\n")
        f.write(new_arr[len(new_arr) - 1])
        print(f"Data saved in file '{newfilename}'")
        f.close()

    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
    except PermissionError as e:
        sys.stderr.write(f"[STDERR] Error opening file '{filename}': {e}\n")
        sys.stderr.flush()
        print("Data not saved.")


if __name__ == "__main__":
    ft_stream_management()
