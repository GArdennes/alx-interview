# 0x0A. Prime Game
For this project, you will need to leverage your understanding of prime numbers, game theory, and algorithm optimization to solve a competitive game scenario. The challenge involves determining the winner of a game based on the strategic removal of prime numbers and their multiples from a set of consecutive integers.
## Learning Objectives
1.Understanding what prime numbers are.
2.Understanding the range of efficient algorithms for identifying prime numbers within a range.
3.Developing a method to count the edges that contribute to the island’s perimeter.
4.Breaking down the problem into smaller, manageable sub-problems with dynamic programming.
6.Implementing functions with efficient looping and conditional statements.


## Tasks
Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming Maria always goes first and both players play optimally, determine who the winner of each game is.

Write a function `def isWinner(x, nums)` where `x` is the number of rounds and `nums` is an array of `n`. Return the name of the player that won the most rounds. If the winner cannot be determined, return `None`. You can assume `n` and `x` will not be larger than 10000. You cannot import any packages in this task.

