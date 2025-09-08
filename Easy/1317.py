class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        def is_valid(n):
            return '0' not in str(n)
        
        for i in range(1, n // 2 + 1):
            if is_valid(i) and is_valid(n - i):
                return [i, n - i]
