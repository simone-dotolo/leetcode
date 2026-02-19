class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        target = '1' if s[0] == '0' else '0'
        prev = 0
        curr = 0
        res = 0

        for i in range(len(s)):
            if s[i] != target:
                curr += 1
                if curr <= prev:
                    res += 1
            else:
                target = '1' if target == '0' else '0'
                prev = curr
                curr = 1
                res += 1
                
        return res
