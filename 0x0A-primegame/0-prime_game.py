#!/usr/bin/python3
"""
0-prime_game
"""


def isWinner(x, nums):
    """
    This function determines the winner of the prime game
    based on number of rounds (x) and list of n values.

    Args:
      x: Number of rounds of the game.
      nums: List of n values for each round.

    Returns:
      "Maria": Maria wins the most rounds.
      "Ben": Ben wins the most rounds.
       None: Winner cannot be determined (tie).
    """
    def sieve(n):
        """ Sieve of Eratosthenes to count primes up to n """
        is_prime = [True] * (n + 1)
        p = 2
        while p * p <= n:
            if is_prime[p]:
                for i in range(p * p, n + 1, p):
                    is_prime[i] = False
            p += 1
        prime_count = [0] * (n + 1)
        count = 0
        for i in range(2, n + 1):
            if is_prime[i]:
                count += 1
            prime_count[i] = count
        return prime_count

    if x <= 0 or not nums:
        return None

    max_n = max(nums)
    prime_count = sieve(max_n)

    maria_wins = 0
    ben_wins = 0

    for n in nums:
        if prime_count[n] % 2 == 1:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None
