class Solution(object):
    def checkOnesSegment(self, s):
        """
        :type s: str
        :rtype: bool
        """
        ones = 0
        last_c = '1'
        for c in s:
            if c == '1':
                if last_c == '0' and ones > 0:
                    return False
                else:
                    ones += 1
            last_c = c
        return True
