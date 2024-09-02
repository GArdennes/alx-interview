## Problem description
We are given a string `expression` that contains a series of fraction additions and subtractions. The task demands that we evaluate the expression and return the result as a simplified fraction in its irreducible form.

## Initial approach

1. We analyse the string considering each character in the string to extract the individual fractions and their corresponding signs or operators.

2. We perform the arithmetic operations on these fractions.

3. We simplify the resulting fraction to its irreducible form.

## Better approach: REGEX

In this approach instead of manually parsing the input string, which can be error-prone. A more compatible method is to use regular expressions (regex) to tokenize the string. For example, if we are given a string `3a4a10`, and we provide `a` as a separator, then the string will be separated into `3`, `4`, and `10`. Thus we need the right separator for the input string.

The regular expression or regex expression of `[+-]?\d+/\d+` is used to find fractions in a string. An input string like `1/2-3/4+5/6` gets split into `['1/2', '-3/4', '+5/6', '7/8']`

To add or subtract fractions, we need to find a common denominator between the currently parsed fraction and the running result. A straightforward appraoch is to use the product of the two denominators as the common denominator. This allows us to rewrite both fractions with this common denominator and then perform the addition or subtraction.

For example, given two fractions:
* Current fraction = $\frac{A}{B}$
* Running result = $\frac{N}{M}$

We can express the sum as:
* new numerator = A x M + N x B
* new denominator = B x M

After we finish processing all the fractions, the resulting fraction may not be in its simplest form. To simply it, we divide the numerator and the denominator by their greatest common divisor (GCD). 

## Example walkthrough correction

**Input:**
expression = "1/3-1/2+1/6"

**Process:**

[1/3, -1/2, 1/6] (regex makes splitting the string into functions easy)

1/3 (first fraction is considered)

-1/2 (second fraction is considered)

-1/6 (subtract -1/2 using a common denominator of 6 i.e. 2/6 - 3/6 = -1/6)

1/6 (third fraction is considered)

0/36 (1/6 is added using a common denominator of 36 i.e. -6/36 + 6/36)

The final result is 0/36 or 0/1