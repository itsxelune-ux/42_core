import sys


def ft_archive_creation() -> None:
    print("=== Cyber Archives Recovery & Preservation ===")
    try:
        argc = len(sys.argv)
        if argc != 2:
            raise ValueError("Usage: python3 ft_ancient_text.py <filename>")
        filename = sys.argv[1]
        print(f"Accessing file '{filename}'")
        f = open(filename, "r")
        string = f.read()
        print("---\n")
        print(string)
        print("\n---")
        arr = string.split('\n')
        f.close()
        print(f"File '{filename}' closed.")

        print("\nTransform data:")
        new_arr = []
        new_arr = [s + "#" for s in arr]
        print("---\n")
        for s in new_arr:
            print(s)
        print("\n---")

        newfilename = input("Enter new file name (or empty): ").strip()
        if not newfilename or newfilename == "":
            raise ValueError("Not saving data.")
        print(f"Saving data to '{newfilename}'")
        f = open(newfilename, "w")
        for i in range(0, len(new_arr) - 1, 1):
            f.write(new_arr[i] + "\n")
        f.write(new_arr[len(new_arr) - 1])
        print(f"Data saved in file '{newfilename}'.")
        f.close()

    except ValueError as e:
        print(e)
    except FileNotFoundError as e:
        print(f"Error opening file '{filename}': {e}")
    except PermissionError as e:
        print(f"Error opening file '{filename}': {e}")


if __name__ == "__main__":
    ft_archive_creation()
