class Solution:
    def numSub(self, s: str) -> int:
        res = 0
        count = 0
        for c in s:
            if c == '1':
                count += 1
            else:
                res += (count * (count + 1)) // 2
                count = 0
        
        if count:
            res += (count * (count + 1)) // 2
        
        return int(res % (1e9 + 7))
