# 0x05. N Queens
The `0x05. N queens` project is a classic problem in computer science and mathematics, known for its application of the backtracking algorithm to place N non-attacking queens on an N×N chessboard. To complete this project, you will need to understand several key concepts and have access to resources that will help you grasp the necessary algorithms and techniques.

## Concepts Needed:
### **Backtracking Algorithms**: Understand how backtracking algorithms work to explore all potential solutions to a problem and backtrack when a solution cannot be completed.

### **Recursion**: Using recursive functions to implement backtracking algorithms.

### **List Manipulations in Python**: Creating and manipulating lists, especially to store the positions of queens on the board.

### **Python Command Line Arguments**: Handling command-line arguments with the `sys` module.

By studying these concepts and utilizing the resources provided, you will be equipped with the knowledge required to implement an efficient solution to the N queens problem using Python. This project not only tests programming and problem-solving skills but also offers an excellent opportunity to learn about algorithmic thinking and optimization techniques.


## Learning
Backtracking is simply a method of finding the right solution through complex options. Backtracking is a problem-solving algorithm that finds a solution to a problem by trying different routes or paths incrementally and backtracking to the last feasible solution when a path leads to a dead end. It can be used to solve puzzles like maze games, or Sudoku. Generally, constraint satisfaction problems are solved with dynamic programming algorithms or greedy algorithms. However, there are situations where dynamic programming struggles and backtracking succeeds. 

Here are some scenarios where backtracking proves to be a better choice than dynamic programming:

**Problem**: Find a path from the starting point to the exit in a maze.

**Backtracking**: Backtracking can explore paths in the maze recursively. At each junction, it would try all possible directions and backtracks if it hits a wall or a dead end. This efficiently explores all valid paths to find an exit.

**Dynamic programming**: Does a choice of path affect the other paths? No, each path is independent of each other and choosing one path does not determine the possible paths of the others. Hence dynamic programming fails.

**Problem**: 

**Backtracking**:

**Dynamic programming**:

#### Pseudocode for Backtracking
```
function Backtrack(problem, currentSolution):
  # Check if currentSolution is a valid solution
  if IsSolution(problem, currentSolution):
    Report(currentSolution)  # Do something with the solution (e.g., store it)
    return

  # Generate candidates for the next step
  candidates = GenerateCandidates(problem, currentSolution)

  # Loop through all possible candidates
  for candidate in candidates:
    # Add candidate to the current solution
    currentSolution.append(candidate)

    # Recursively explore possibilities with the new candidate
    Backtrack(problem, currentSolution)

    # Remove candidate from the current solution (backtracking)
    currentSolution.pop()
```

#### Rat in a Maze using Backtracking
Step-by-step approach
1. Create `is_valid` function to check if a cell at position (x, y) is inside the maze and unblocked.
2. Create `solve_maze` to get all valid paths:
a. Base case: If the current position is the bottom-right cell, which is the destination, add the current path to the result and return.
b. Mark the current cell as blocked.
c. Iterate through all possible directions.
i. Calculate the next position based on the current direction
ii. If the next position is valid (i.e. `is_valid` returns `true`), append the direction to the current path and recursively call the `solve_maze` function for the next cell.
iii. Backtrack by removing the last direction from the current path.
d. Mark the current cell as un-blocked before returning.

```
def is_valid(maze, row, col):
  """
  Checks if a cell is within the maze boundaries and not a wall.
  """
  return 0 <= row < len(maze) and 0 <= col < len(maze[0]) and maze[row][col] != 1

def solve_maze(maze, row, col):
  """
  Solves the rat in a maze problem recursively using backtracking.
  """
  # Base case: Reached the destination (bottom right corner)
  if row == len(maze) - 1 and col == len(maze[0]) - 1:
    return True

  # Mark current cell as visited
  maze[row][col] = 2

  # Try all valid moves (down, right, up, left)
  for (dx, dy) in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
    next_row = row + dx
    next_col = col + dy

    # Check if the next move is valid
    if is_valid(maze, next_row, next_col):
      # Recursively explore the path from the next cell
      if solve_maze(maze, next_row, next_col):
        return True

  # Backtrack if no valid move leads to the destination
  maze[row][col] = 0  # Unmark the cell
  return False

def print_maze(maze):
  """
  Prints the maze with the solution path marked as 'X'.
  """
  for row in maze:
    for cell in row:
      if cell == 0:
        print(".", end=" ")
      elif cell == 1:
        print("W", end=" ")  # Print "W" for walls
      else:
        print("X", end=" ")  # Print "X" for the solution path
    print()

# Sample maze (0: empty, 1: wall)
maze = [
    [0, 0, 0, 0],
    [0, 1, 0, 0],
    [0, 1, 0, 1],
    [0, 0, 0, 0],
]

# Starting position (replace with desired starting position)
start_row = 0
start_col = 0

# Solve the maze and print the solution
if solve_maze(maze, start_row, start_col):
  print("Maze Solved:")
  print_maze(maze)
else:
  print("No solution found!")
```

## Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted/compiled on Ubuntu 20.04 LTS using `python3`
- All your files should end with a new line.
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A readme file, at the root of the folder of the project, is mandatory.
- Your code should use the `PEP 8` style.
- All your files must be executable

## Tasks
The N queens puzzle is the challenge of placing N non-attacking queens on a NxN chessboard. Write a program that solves the N queens problem.

**Requirements**
- Usage: `nqueens N`
- If the user called the program with the wrong number of arguments, print `Usage: nqueens N`, followed by a new line, and exit with the status `1`.
- N must be an integer greater or equal to 4
- If N is not an integer, print `N must be a number`, followed by a new line, and exit with the status `1`.
- If N is smaller than `4`, print `N must be at least 4`, followed by a new line, and exit with the status `1`.
- The program should print every possible solution to the problem, one solution per line.
- You are only allowed to import the `sys` module
