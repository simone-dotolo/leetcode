class Solution:
    def minimumPushes(self, word: str) -> int:
        l = len(word)
        c = 1
        res = 0
        while l >= 8:
            res += (c * 8)
            c += 1
            l -= 8
        
        res += (c * l)
        return res
