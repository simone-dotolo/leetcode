class Solution(object):
    def concatenatedBinary(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        for i in range(1, n + 1):
            res *= 2 ** len(bin(i)[2:])
            res += i
            res = res % (1e9 + 7)
        return int(res)
