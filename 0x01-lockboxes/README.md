# 0x01. Lockboxes
## Must Know
### Concepts Needed:
1) Lists and List Manipulation:
Understanding how to work with lists, including accessing elements, iterating over lists, and modifying lists dynamically.
2) Graph Theory Basics:
Although not explicitly required, knowledge of graph theory (especially concepts related to traversal algorithms like Depth-First Search or Breadth-First Search) can be very helpful in solving this problem, as the boxes and keys can be thought of as nodes and edges in a graph.
3) Algorithmic Complexity:
Understanding the time and space complexity of your solution is important, as it can help in writing more efficient algorithms.
4) Recursion:
Some solutions might require a recursive approach to traverse through the boxes and keys.
5) Queue and Stack:
Knowing how to use queues and stacks is crucial if implementing a breadth-first search (BFS) or depth-first search (DFS) algorithm to traverse through the keys and boxes.
6) Set Operations:
Understanding how to use sets for keeping track of visited boxes and available keys can optimize the search process.

## Requirements
1) Allowed editors: vi, vim, emacs
2) All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3
3) All your files should end with a new line
4) The first line of all your files should be exactly #!/usr/bin/python3
5) A readme file, at the root of the folder of the project, is mandatory
6) Your code should be documented
7) Your code should use the PEP 8 style
8) All your files must be executable

## Tasks
### 0. Lockboxes
You have n number of locked boxes in front of you. Each box is numbered sequentially from 0 to n - 1 and each box may contain keys to the other boxes.
Write a method that determines if all the boxes can be opened.
Prototype: def canUnlockAll(boxes)
boxes is a list of lists
A key with the same number as a box opens that box
You can assume all keys will be positive integers
There can be keys that do not have boxes
The first box boxes[0] is unlocked
Return True if all boxes can be opened, else return False

