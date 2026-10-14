class Solution:
    def maxSumOfSquares(self, num: int, sum: int) -> str:
        res = ''

        for _ in range(num):
            digit = min(9, sum)
            sum -= digit
            res += str(digit)
        
        if sum != 0:
            return ''
        
        return res
