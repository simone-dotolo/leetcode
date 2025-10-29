class Solution:
    def smallestNumber(self, n: int) -> int:
        from math import ceil, log
        return int(2 ** int(log(n, 2) + 1)) - 1
