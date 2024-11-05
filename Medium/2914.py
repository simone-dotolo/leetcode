class Solution:
    def minChanges(self, s: str) -> int:
        res = 0
        first = True
        prev = 0

        for el in s:
            if not first:
                first = True
                if el != prev:
                    res += 1
            else:
                first = False
            prev = el
        
        return res
