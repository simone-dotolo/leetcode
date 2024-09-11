class Solution:
    def numSteps(self, s: str) -> int:
        n = len(s)
        num = 0
        ans = 0

        num = int(s,2)
        
        while num != 1:
            if num % 2 == 0:
                num = num >> 1
            else:
                num += 1
            ans += 1

        return ans