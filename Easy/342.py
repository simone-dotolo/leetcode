class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        return log(n, 4) == float(floor(log(n, 4)))
        
