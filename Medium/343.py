class Solution:
    def integerBreak(self, n: int) -> int:
        cache = {}

        def dp(i):

            if(i <= 1):
                return 1
            
            if(i in cache):
                return cache[i]

            cache[i] = max([j * max(dp(i-j),i-j) for j in range(1,i)])

            return cache[i]
        
        return dp(n)