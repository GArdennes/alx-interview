## Problem description
The goal is to find the difference between two pairs of the numbers in the array. 
The difference that happens to be the least is the smallest distance. 

### Uncertainty
How does the k<sup>th</sup> make any difference?

### Example
Given:
* nums = [1, 6, 1]
* k = 3

**All pairs and their distances:**
* (1, 6) -> distance = 5
* (1, 1) -> distance = 0
* (6, 1) -> distance = 5

**Sorted distances:** [0, 5, 5]

**k-th smallest:** for k = 3, the 3rd smallest distance is 5

## Initial approach (Brute force)
1. Get the length of the list of numbers
2. Initialize an integer list variable "distance" to empty with a length equal to the length of the list of numbers 
3. Using two loops traverse the list;
    * The first would traverse from the first element to the last
    * The second would traverse from the second to the first element
    * The difference between the elements of the two indexes from the loops would be taken
    * Populate the distance list with the difference values
4. Sort the list of distances.
5. Return the kth element in the distances list.

## Recommended approach(Binary Search with Two-pointer method)
1. The first step is to sort the array of numbers. Sorting is crucial because it allows us to efficiently use the two-pointer technique.
2. Initialize two variables low and high, to track the lowest possible distance and the other to track the highest possible distance.
3. Binary search is performed over the range [low, high], where mid is the middle distance being considered.
4. For each mid, the code checks how many pairs of elements in nums have a distance less than or equal to mid using the `countPairs` function.
    * The function calculates the number of pairs (i, j) such that the distance `nums[j] - nums[i] <= mid` where i < j.
    * First the variables, count, left and right are initialized.
    * Left and right are simply pointers to i and j.
    * For each right, left is increased while the distance `nums[right] - nums[left]` is greater than mid else;
        * The distance between left and right is $\leq$ mid.
        * The count variable is increased by the difference between right and left.
    * The function returns the sum of these counts for all possible right values.
5. If the number of such pairs is greater than or equal to `k`, it means the k-th smallest distance is less than or equal to mid, so we reduce the search space by setting high = mid.
6. Otherwise, if fewer than k pairs from `countPairs` have a distance $\leq$ mid, it means the k-th smallest distance is greater than mid, so we set low = mid + 1.
7. Until low = high, then we have our least k-th distance.

## Example walkthrough
`nums = [1, 3, 1]` and `k = 1`

1. Sorting gives `nums = [1, 1, 3]`
2. The range for binary search is `low = 0` and `high is 2`.
3. Our `mid = 1`
4. What are the number of pairs with difference less than mid.
5. Our first pair nums[0] - nums[0] = 0, has a difference less than mid of 1. We count this pair as 1.
6. Second pair nums[1] - nums[0] = 0 counts as pair 2.
7. Third pair nums[2] - nums[0] = 2 is greater than mid. We increase the second index from nums[0] to nums[1].
8. Another pair nums[2] - nums[1] = 2 is greater than mid. We increase the second index again.
9. Last pair nums[2] - nums[2] = 0 counts as 0, we return a count of 2
10. Since the return value of countPairs() is equal to k=1, high becomes 1.
---
11. We enter into the second iteration of the loop. Since low = 0 is less than high = 1
12. Our mid is (0 + 1) // 2 = 0
13. What are the number of pairs with difference less than mid (0)
14. For nums[0] - nums[0] = 0. No valid pair since difference is 0 which is not less than 0.
15. For nums[1] - nums[0] = 0. Pair count is increased by 1.
16. For nums[2] - nums[0] = 1. We increase the left index, nums[0] becomes nums[1], we increase again nums[1] becomes nums[2] but still no valid counts.
17. Since the count (1) is $\geq$ k (1), high = mid = 0.
18. Now low = high = 0, so the loop exists and returns low, which is 0. The answer is 0.

