class Solution(object):
    def getDescentPeriods(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        res = 1
        curr = 1
        for i in range(1, len(prices)):
            if prices[i] == prices[i - 1] - 1:
                curr += 1
            else:
                curr = 1
            res += curr
        return res
