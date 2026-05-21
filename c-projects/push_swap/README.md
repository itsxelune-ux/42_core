*This project has been created as part of the 42 curriculum by omitrovs.*

# push_swap

## Description

**push_swap** is a sorting algorithm project from the 42 curriculum.  
The goal of this project is to sort a stack of integers using a limited set of predefined operations, while producing the smallest possible number of moves.

The program receives a list of integers as arguments and outputs a sequence of operations that sorts the numbers in ascending order.

For this implementation, I used the **Turk Algorithm**, an optimized cost-based strategy designed to minimize the total number of operations by calculating the cheapest move at each step.

I decided to use the Turk Algorithm because it felt like a good balance between performance and clarity. I didn’t want something extremely complicated, and i also wanted an algorithm thats known well around this project.


### Project Goals

- Implement a sorting algorithm using only allowed stack operations.
- Optimize the number of operations.
- Handle errors and invalid input correctly.
- Respect the 42 Norm and memory management rules.

---

## Instructions

### Compilation

To compile the project:

```bash

make        # Compile push_swap
make clean  # Remove object files
make fclean # Remove object files and executable
make re     # Recompile everything

```

### Usage

Run the program with a list of integers:

```bash
./push_swap 3 2 5 1 4
```

The program will output a list of operations such as:

```bash
pb
ra
sa
pa
```
To test the result using the checker:

```bash
ARG="3 2 5 1 4"; ./push_swap $ARG | ./checker_linux $ARG
```

### Error Handling

The program handles:

- Non-numeric arguments

- Duplicate numbers

- Integer overflow

- Empty input

### Algorithm – Turk Algorithm Strategy

The Turk Algorithm works as follows:

- Push all elements except three to stack B.
	- Note: This step was optimized by:
		1. Calculating the median (`median = sum / size`).
		2. After pushing 1 element, check if this element is below the median.
		3. If that's the case, rotate this element in stack B.

- Sort the remaining three elements in stack A.

- For each element in stack B:

	- Find the *target node*. This node should be:
		1. Higher than element in stack A,
		2. The minimal node.
		3. If any of these conditions are not satisfied, push on top of the minimal node of A.
		- Note: Target node is the node in A, which on top of this node the element in stack B should be pushed.

	- Calculate the cost of moving it to the correct position in stack A.
		- Note: Cost is the number of rotations to push this element on the top of stack.

	- Determine the cheapest move.

	- Execute combined rotations when possible (rr / rrr) to minimize operations.
	- Push element back to stack A.

- Rotate stack A to place the smallest number at the top.

---

## Resources

### Documentation & References

- 42 push_swap subject PDF
- [Linked list documentation](https://www.geeksforgeeks.org/dsa/singly-linked-list-tutorial/)
- [Documentation on stack data structures](https://www.geeksforgeeks.org/c/implement-stack-in-c/)
- [Turk algorithm explained in 6 steps](https://pure-forest.medium.com/push-swap-turk-algorithm-explained-in-6-steps-4c6650a458c0)
- [Big-O time complexity documentation](https://www.geeksforgeeks.org/dsa/analysis-algorithms-big-o-analysis/)

---

## AI Usage Disclosure

I used AI mainly for:
- Understanding optimization concepts related to the Turk Algorithm
- Clarifying theoretical aspects of cost calculation
- Improving documentation and README structure

