#!/usr/bin/env python3
'''
0-minoperations
'''
from typing import List


def calcPrimes(n: int) -> List[int]:
    '''
    Calculates the list of prime factors of n.
    '''
    prime_fac = []
    if n <= 1:
        return prime_fac
    i = 2
    while i * i <= n:
        if n % i == 0:
            prime_fac.append(i)
            n //= i
        else:
            i += 1
    if i > 1:
        prime_fac.append(i)
    return prime_fac


def minOperations(n: int) -> int:
    '''
    Calculates the fewest number of operations needed
    to result in exactly n H characters in the file.
    '''
    if n <= 1:
        return 0
    prime_fac = calcPrimes(n)
    return sum(prime_fac)
