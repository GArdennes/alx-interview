## Problem description

Given a grid of m rows and n columns, you are to return the sum of a number from each row that gives the hightest possible value considering loss points are subtracted.

## Initial approach

1. Initialize a variable to track the column index, and the cummulative maximum point
2. Declare the cummulative maximum point, maximum point, current column index, previous column index, column difference count to be 0
3. Traverse the arrays with a for loop.

    a. For each row, for each column;

        * if the value of that cell is greater than maximum point, then the max point is updated to this point value. Also the column index is recorded.

        * Else it is ignored

    b. For each row;

        * the maximum points are summed into the cummulative maximum point

        * If the current column index differs from the previous column index the difference is recorded as column difference count.

4. The column difference count is subtracted from the cummulative sum and the result is returned.

## Issues with the approach
* The approach uses a greedy strategy of picking the maximum point in each row, but  this is not always optimal. For example, if switching to a maximum point in the next row incurs a large penalty due to the column difference, it might be better to pick a suboptimal value in the current row to minimize the penalty. The column difference penalty should influence the decision of which cell to pick in each row and should not be considered afterward.

## Better approach: Dynamic programming

For each row, we keep track of the best possible score for each column, considering the penalties incurred when transitioning from the previous row.

A dp[n] array would be necessary to keep track of the best score possible, if we end up selecting column n in the current row.

For each row m:
1. We compute the potential scores by considering penalties using a left-to-right pass.
2. We compute the potential scores by considering penalties using a right-to-left pass.

### Left-to-right pass
We consider moving from the left to right, in such a way as to record not only our best values but also consider the penalty of switching columns.

A convenient formula that processes this problem efficiently with dynamic programming would be;

```python
left_max[j] = max(left_max[j - 1] - 1, dp[j])
```

For each column j, dp[j] is populated with the value at the index of the former row,then the maximum value counting from the left would be left_max. We consider the penalty for moving across columns with `-j`.

### Right-to-left pass
We would follow a similar pattern as the left to right pass, bear in mind the movement is in the opposite direction;

```python
right_max[j] = max(right[j + 1] - 1, dp[j])
```

For each column j, dp[j] is populated with the value at the index of the former row, then the maximum value counting from the right would be right_max. We consider the penalty for moving across columns with `-j`.

### Aggregated points

```python
new_dp[j] = points[i][j] + max(left[j], right[j])
```

The new dp array for the columns keeps track of the points we would earn.

## Example walkthrough correction

**Input:** 
points = [[1, 2, 3], [1, 5, 1], [3, 1, 1]]

**Process:**

first row (i = 0), initialization:

dp = [1, 2, 3]

First iteration (i = 1). Our second row.

* peforming the left-to-right pass:

left_max = [0, 0, 0] (our left pass array is initialized.)

left_max[0] = dp[0] (our initial case is the value for the first element which from the grid 1)

left_max = [1, 0, 0]

left_max[j] = max(left_max[j - 1] - 1, dp[j]) (for each column starting from the second, j = 1, we find the maximum possible value. Starting from the second column means the introduction of the penalty `-1`.)

for j = 1:

left_max[1] = max(left_max[0] - 1, dp[1])  

left_max[1] = max(1 - 1, 2)

left_max[1] = 2 (left_max = [1, 2, 0])

for j = 2:

left_max[2] = max(left_max[2 - 1] - 1, dp[2]) 

left_max[2] = max(left_max[1] - 1, 3)

left_max[2] = max(1, 3)

left_max[2] = 3 (left_max = [1, 2, 3])

* peforming the right-to-left pass:

right_max = [0, 0, 0]

right_max[-1] = dp[-1]

right_max = [0, 0, 3]

right_max[j] = max(right_max[j + 1] - 1, dp[j]) (for each column j, from right to left, the loop starts with j initialized to n - 2 and decrements by 1 in each iteration until it reaches 0.)

for j = 1

right_max[1] = max(right_max[1 + 1] - 1, dp[1])

right_max[1] = max(right_max[2] - 1, dp[1])

right_max[1] = max(2, 2)

right_max[1] = 2 (right_max = [0, 2, 3])

for j = 0

right_max[0] = max(right_max[0 + 1] - 1, dp[0])

right_max[0] = max(right_max[1] - 1, dp[0])

right_max[0] = max(1, 1)

right_max[0] = 1 (right_max = [1, 2, 3])

After conducting our right-to-left pass we should get the points for both passes. We then need to calculate the new_dp for the second row (points[1] = [1, 5, 1]).

* finding our points for current row

dp[j] = points[i][j] + max(left_max[j], right_max[j])

for j = 0

dp[0] = points[1][0] + max(left_max[0], right_max[0])

dp[0] = 1 + max(1, 1)

dp[0] = 2

for j = 1

dp[1] = points[1][1] + max(left_max[1], right_max[1])

dp[1] = 5 + max(2, 2)

dp[1] = 7

for j = 2

dp[2] = points[1][2] + max(left_max[2], right_max[2])

dp[2] = 1 + max(3, 3)

dp[2] = 4

Our dp array of maximum points for the second row is [2, 7, 4]

Second iteration (i = 2). Our third row.

* performing left-to-right pass

rememeber our dp is now [2, 7, 4]

left_max = [0, 0, 0]

for j = 0

left_max = [2, 0, 0]

for j = 1

left_max = [2, 7, 0]

for j = 2

left_max = [2, 7, 6]

* performing right-to-left pass:

right_max = [0, 0, 0]

for j = 2

right_max = [0, 0, 4]

for j = 1

right_max = [0, 7, 4]

for j = 0

right_max = [6, 7, 4]

* finding our points for current row

points[2] = [3, 1, 1]

left_max = [2, 7, 6]

right_max = [6, 7, 4]

dp[0] = points[2][0] + max(left[0], right[0])

dp[0] = 9

dp[1] = points[2][1] + max(left[1], right[1])

dp[1] = 8

dp[2] = points[2][2] + max(left[2], right[2])

dp[2] = 7

dp = [9, 8, 7]

max(dp) = 9

**Output:**
9