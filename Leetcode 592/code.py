import re
from fractions import gcd

class Solution(object):
    def fractionAddition(self, expression):
        """
        :type expression: str
        :rtype: str
        """
        fractions = re.findall('[+-]?\d+/\d+', expression)
        numerator, denominator = 0, 1
        for fraction in fractions:
            num, denom = map(int, fraction.split('/'))
            numerator = numerator * denom + num * denominator
            denominator *= denom
            common_divisor = gcd(abs(numerator), denominator)
            numerator //= common_divisor
            denominator //= common_divisor
        
        if denominator < 0:
            numerator, denominator = -numerator, -denominator
        return f"{numerator}/{denominator}"
