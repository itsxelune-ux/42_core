*This project has been created as part of the 42 curriculum by omitrovs.*

# Get Next Line

## Description
The goal of the Get Next Line project is to implement a function called `get_next_line` that reads one line at a time from a given file descriptor. A line is defined as a sequence of characters ending with a newline character `\n` or the end of the file. The function returns the line including the newline character, except if it reaches the end of the file without a trailing newline.

This project focuses on several key programming concepts in C:
- Reading data from files efficiently using the `read()` system call.
- Managing memory dynamically with `malloc()` and `free()`.
- Using static variables to maintain state between function calls.
- Handling edge cases, such as empty files, very small or very large buffer sizes, and memory allocation failures.

Repeated calls to `get_next_line` allow reading an entire file, one line at a time, without reading the whole file into memory at once. This makes it efficient for large files and a good exercise in careful memory management.

---

## How It Works

The algorithm I implemented works in the following steps:

1. **Static Buffer (`stash`)**  
   A static variable is used to store leftover data that was read but not yet returned. This allows `get_next_line` to remember what was left from previous reads between calls.

2. **Reading the File**  
   The function reads from the file descriptor in chunks of size `BUFFER_SIZE`. It stops reading as soon as it encounters a newline character or reaches the end of the file.

3. **Extracting a Line**  
   Once a newline character is found (or end-of-file is reached), the function extracts the line from the `stash` and returns it.

4. **Updating the Stash**  
   After returning a line, the function updates the `stash` to remove the returned line, keeping only the remaining part for the next call.

5. **Memory Management**  
   Every allocation is carefully freed to avoid memory leaks. The `stash` is freed when no longer needed, and each returned line should also be freed by the caller.

---

## Instructions

### Compilation
To compile the project, use the following command. You can define `BUFFER_SIZE` to any positive integer. For example:

```bash
# Compile with BUFFER_SIZE set to 42
cc -Wall -Wextra -Werror -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c -o gnl
```

---

## Resources

- Linux manual pages: `man 2 read`
- Unix/Linux file descriptor documentation
- Official 42 Get Next Line subject PDF
- GNU C Library documentation

---

## Use of AI

AI tools were used only for learning and clarification purposes.

AI was used to:
- Understand Unix/Linux concepts such as file descriptors and the `read()` system call
- Review algorithm ideas and edge cases at a conceptual level

All code was written, tested, and debugged manually by me, in accordance with the 42 school rules.