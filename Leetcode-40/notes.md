## Approach
To solve this problem, there is the need to outline our approach.

### Steps
1. Considering each number in the `candidates` array can only be used once in each combination, we need to avoid duplicates. Sorting the candidates in ascending order helps to skip duplicates.
2. We need to find all unique combinations of numbers from the `candidates` array that sum up to the `target` value. Techniques available for finding all the unique combinations are Backtracking, Dynamic Programming (DP), Breadth-First Search (BFS) and Depth-First Search (DFS). However, Backtracking is the most efficient memory and computational wise.
3. Backtracking:
   * Start with an empty combination for each candidate.
   * If a candidate is added, recursively try adding the next candidates to see if they reach the target sum.
   * If the sum exceeds the target, stop and backtrack to explore other possibilities.
   * Skip duplicates to ensure that we don't generate teh same combination multiple times.