class Solution:
    def minOperations(self, s: str) -> int:
        res = 0
        prev = s[0]
        for c in s[1:]:
            if c == prev:
                res += 1
            prev = '1' if prev == '0' else '0'
        return min(res, len(s) - res)
