# 0x08. Making Change
For this project, you will need to apply your knowledge of algorithms, data structures, and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers. Understanding how to navigate and analyze 2D arrays and apply logical operations to determine the conditions for perimeter calculation is crucial for this task.
## Learning Objectives
1.Understanding how to navigate through adjacent cells (horizontally and vertically).
2.Understanding when to apply conditions that determine whether a cell contributes to the perimeter of the island.
3.Developing a method to count the edges that contribute to the island’s perimeter.
4.Breaking down the problem into smaller tasks, such as identifying land cells and calculating their contribution to the perimeter.
5.Breaking down the problem into smaller, manageable sub-problems.
6.Implementing functions with efficient looping and conditional statements.


## Tasks
### 0. Island Perimeter
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`. `grid` is a list of list of integers: 0 represents water, 1 represents land, each cell is square, with a side length of 1. Cells are connected horizontally/vertically (not diagonally). `grid` is rectangular, with its width and height not exceeding 100. The grid is completely surrounded by water and there is only one island (or nothing). The island doesn’t have ‘lakes’ (water inside that isn’t connected to the water surrounding the island).
