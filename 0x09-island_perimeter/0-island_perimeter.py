#!/usr/bin/python3
"""
0-island_perimeter
"""


def island_perimeter(grid):
    """
    This function returns the perimeter of the island described in the grid

    Args:
      grid: The grid of land and water
    Returns:
      The perimeter of the island
    """
    if not all(isinstance(row, list) for row in grid):
        return 0

    perimeter = 0

    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                if row == 0 or grid[row - 1][col] == 0:
                    perimeter += 1
                if row == rows - 1 or grid[row + 1][col] == 0:
                    perimeter += 1
                if col == 0 or grid[row][col - 1] == 0:
                    perimeter += 1
                if col == cols - 1 or grid[row][col + 1] == 0:
                    perimeter += 1
    return perimeter
