class Solution(object):
    def findFinalValue(self, nums, original):
        """
        :type nums: List[int]
        :type original: int
        :rtype: int
        """
        res = 0
        for num in nums:
            if num % original == 0:
                div = num // original
                if div & (div - 1) == 0:
                    res = res | div

        for i, digit in enumerate(bin(res)[::-1]):
            if digit == '0' or digit == 'b':
                return 2 ** i * original
