## Problem description

The problem requires us to find the minimum number of times a particular character 'A' can be printed on a screen 'n' times, if the only operations we have are copy all and paste. 

After long deliberation, and some help, I realize the problem is about finding the factorization of 'n' and using the factors to determine how many operations are needed.

## Initial approach (Brute force)

If `n = 9`, what we can do is this:
1. Start with one `A`.
2. Copy it, and then paste it 2 times to get 3 `A`s (total 3 operations).
3. Then copy all 3 `A`s and paste it 2 times to get 9 `A`s (total 3 more operations).

The prime numbers of 9 are 3 and 3.

## Better approach: Dynamic programming

When adding A's on the screen to achieve `n` A's, we note that it is unnecessary to apply consecutive Copy All operations because applying consecutive Copy All operations has the same effect as applying just one. If a Copy All operation is applied, then a Paste operation should be applied right after. Thus, we have two options to add A's on the screen at every step:

1. Apply a copy all operation first and then apply the paste operation right after.
2. Apply a paste operation.

A function recommended is `f(i)`, which represents the minimum number of operations needed to get to `i` A's starting with 1 A. One possible way to make `i` A's is to use the Copy All operation on `j` A's, where `j` is a factor of `i`. We can then paste the `j` A's `(i - j)/j` times to reach a total of `i` A's. If this approach is chosen, then the minimum number of operations possible would be `f(j) + 1 + (i - j)/j`. Here, `f(j)` represents the minimum number of operations to reach `j` A's, `1` accounts for the single Copy All operation on the `j` A's, and `(i - j)/j` represents the number of additional Paste operations of `j` A's needed.

We can simplify the expression `f(j) + 1 + (i - j)/j` to `f(j) + i/j`.

## Example walkthrough
Suppose we want to find the minimum number of operations to get exactly `n = 9` A's.

**Input:**
n = 9


**Process:**

* initial setup

    dp = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    dp[1] = 0 (the least number of steps required to get 1 A on screen is 0)

* for i = 2 (the outer loop iterates through each i from 2 to n or 9.)

    dp[2] = 2 (1 copy and 1 paste)

    j = 1 (we are looking for the divisors of 2)

    2 % 1 == 0 

    dp[2] = min(dp[2], dp[1] + 2)

    dp[2] = min(2, 2)

    dp[2] = 2

* for i = 3

    dp[3] = 3 (1 copy and 2 pastes)

    j = 1

    3 % 1 == 0

    dp[3] = min(dp[3], dp[1] + 3)

    dp[3] = min(3, 3)

    dp[3] = 3

* for i = 4

    dp[4] = 4

    range (1, 3)

    j = 1

    4 % 1 == 0 (dp[4] can be obtained by first getting `1` A and then performing `4 // 1 = 4` pastes.)

    dp[4] = min(dp[4], dp[1] + 4)

    dp[4] = min(4, 4)

    dp[4] = 4

    j = 2

    4 % 2 == 0 (dp[4] can be obtained by first getting `2` A's using dp[2] and then performing `4 // 2 = 2` pastes.)

    dp[4] = min(dp[4], dp[2] + 2)

    dp[4] = 4

    j = 3

    4 % 3 != 0 (so we skip)

* for i = 5

    dp[5] = 5 (1 copy and 4 pastes)

    range(1, 2 + 1)

    j = 1

    5 % 1 == 0

    dp[5] = min(dp[5], dp[1] + 5)

    dp[5] = 5

    j = 2

    5 % 2 != 0 (so we skip)

    j = 3

    5 % 3 != 0 (so we skip)

* for i = 6

    dp[6] = 6

    range(1, 2 + 1)

    j = 1

    dp[6] = min(dp[6], dp[1] + 6)

    dp[6] = 6

    j = 2

    dp[6] = min(dp[6], dp[2] + 3)

    dp[6] = 5

    j = 3

    dp[6] = min(dp[6], dp[3] + 2)

    dp[6] = 5

* for i = 7

    dp[7] = 7

    range(1, 3 + 1)

    j = 1

    dp[7] = min(dp[7], dp[1] + 7)

    dp[7] = 7

    j = 2

    7 % 2 != 0

    j = 3

    7 % 3 != 0

    7 % 4 != 0

* for i = 8

    dp[8] = 8

    range(1, 3 + 1)

    j = 1

    dp[8] = 8

    j = 2

    dp[8] = min(dp[8], dp[2] + 4)

    dp[4] = 6

    j = 3

    8 % 3 != 0

    j = 4

    dp[8] = min(dp[8], dp[4] + 2) (dp = [0, 0, 2, 3, 4, 5, 5, 7, 0, 0])

    dp[8] = min(8, 4 + 2)

    dp[8] = 6

* for i = 9

    dp[9] = 9

    range(1, 3 + 1)

    j = 1

    dp[9] = 9

    j = 2

    9 % 2 !=0

    j = 3

    9 % 3 == 0

    dp[9] = min(dp[9], dp[3] + 3)

    dp[9] = min(9, 6)

    dp[9] = 6

    j = 4

    9 % 4 != 0

dp = [0, 0, 2, 3, 4, 5, 5, 7, 6, 6]

**Output:** 
6

