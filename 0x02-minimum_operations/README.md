# 0x02. Minimum Operations
For this project, you will need to understand several key algorithmic and mathematical concepts to devise a solution that efficiently calculates the minimum number of operations to achieve a given number of characters using only “Copy All” and “Paste” operations. Here is a list of concepts and resources that will be helpful:

## Concepts Needed:
1) Dynamic Programming:
a) Familiarity with dynamic programming can help in breaking down the problem into simpler subproblems and building up the solution.
2) Prime Factorization:
a) Understanding how to perform prime factorization is crucial since the problem can be reduced to finding the sum of the prime factors of the target number n.
3) Code Optimization:
a) Knowing how to approach problems from an optimization perspective can be useful in finding the most efficient solution.
4) Greedy Algorithms:
a) The problem can also be approached with greedy algorithms, choosing the best option at each step.
5) Basic Python Programming:
a) Proficiency in Python, including loops, conditionals, and functions, is necessary to implement the solution.
By studying these concepts and utilizing the resources provided, you will be equipped to tackle the “Minimum Operations” problem effectively, applying both mathematical reasoning and programming skills to find the most efficient solution.

## Requirements
1) Allowed editors: vi, vim, emacs
2) All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3
3) All your files should end with a new line
4) The first line of all your files should be exactly #!/usr/bin/python3
5) A readme.md file, at the root of the folder of the project, is mandatory
6) Your code should be documented
7) Your code should use the PEP 8 style
8) All your files must be executable

## Tasks
### 0. Minimum Operations
In a text file, there is a single character H. Your text editor can execute only two operations in this file: Copy All and Paste. Given a number n, write a method that calculates the fewest number of operations needed to result in exactly n H characters in the file.
Prototype: def minOperations(n)
Returns an integer
If n is impossible to achieve, return 0
