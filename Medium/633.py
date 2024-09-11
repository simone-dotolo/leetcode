class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        from math import sqrt

        left = 0
        right = int(sqrt(c)) + 1

        while left <= right:
            res = left**2 + right**2
            if res == c:
                return True
            elif res < c:
                left += 1
            else:
                right -= 1
        
        return False