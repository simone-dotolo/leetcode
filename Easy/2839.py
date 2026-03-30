class Solution(object):
    def canBeEqual(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        s1 = [c for c in s1]
        s2 = [c for c in s2]
        for i in range(4):
            if s1[i] != s2[i]:
                if i < 2:
                    if s1[i] != s2[i+2]:
                        return False
                    s2[i], s2[i+2] = s2[i+2], s2[i]
                else:
                    return False
        return True
