class Solution:
    def nthUglyNumber(self, n: int) -> int:
        ugly = [0] * n
        ugly[0] = 1

        p2 = p3 = p5 = 0

        next_multiple_of_2 = 2
        next_multiple_of_3 = 3
        next_multiple_of_5 = 5

        for i in range(1, n):
            next_ugly = min(next_multiple_of_2, next_multiple_of_3, next_multiple_of_5)
            ugly[i] = next_ugly

            if next_ugly == next_multiple_of_2:
                p2 += 1
                next_multiple_of_2 = ugly[p2] * 2
            if next_ugly == next_multiple_of_3:
                p3 += 1
                next_multiple_of_3 = ugly[p3] * 3
            if next_ugly == next_multiple_of_5:
                p5 += 1
                next_multiple_of_5 = ugly[p5] * 5
        return ugly[-1]
