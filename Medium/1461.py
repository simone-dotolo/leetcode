class Solution(object):
    def hasAllCodes(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: bool
        """
        seen = [False for _ in range(2**k)]
        for i in range(len(s) - k + 1):
            seen[int(s[i:i+k], 2)] = True
        return sum(seen) == 2**k
