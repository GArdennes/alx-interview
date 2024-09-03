## Example walkthrough correction
**Input:**
n = 123

**Process:**

length = len(n) (length = 3 because the input string '123' has 3 characters)

n != 1 (if n == '1' is skipped)

candidates.add(str(10 ** (length - 1) -1)) 

candidates.add(str(10 ** 2 - 1))

candidates.add(str(99))

candidates.add(str(10 ** length + 1))

candidates.add(str(10 ** 3 + 1))

candidates.add(str(1001))

prefix = int(n[:(length + 1) // 2])

prefix = int(n[:2])

prefix = 12

for i = -1

new_prefix = str(prefix + i)

new_prefix = str(12 - 1)

new_prefix = '11'

candidates.add(new_prefix + new_prefix[-2::-1]) (new_prefix[-2::-1] slices new_prefix starting from the index -2 to the beginning in reverse)

candidates.add('11' + '1')

candidates.add('111')

for i = 0

new_prefix = str(12 - 0)

new_prefix = '12'

candidates.add(new_prefix + new_prefix[-2::-1])

candidates.add('12' + '1')

candidates.add('121')

for i = 1

new_prefix = str(12 + 1)

new_prefix = '13'

candidates.add('13' + '1')

candidates.add('131') (candidates is now (99, 1001, 111, 121, 131))

closest = min(candidates, key=lambda x:(abs(int(x) - int(n)), int(x)))

for '99': abs(99 - 123) = 24

for '1001': abs(1001 - 123) = 878

for '111': abs(111 - 123) = 12

for '121': abs(121 - 123) = 2

for '131': abs(131 - 123) = 8

return closest (the smallest difference is 2 for '121')

**Output:**
121