class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)

        if n == '1':
            return '0'
        candidates = set()
        candidates.add(str(10 ** (length - 1) - 1))
        candidates.add(str(10 ** length + 1))
        prefix = int(n[:(length + 1) // 2])
        for i in [-1, 0, 1]:
            new_prefix = str(prefix + i)
            if length % 2 == 0:
                candidates.add(new_prefix + new_prefix[::-1])
            else:
                candidates.add(new_prefix + new_prefix[-2::-1])
        
        candidates.discard(n)

        closest = min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))

        return closest