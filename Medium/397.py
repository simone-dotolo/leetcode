class Solution:
    def integerReplacement(self, n: int) -> int:

        from math import inf

        cache = {}

        def dp(i):

            if i == 1:
                return 0
            
            if i < 1:
                return inf
            
            if(i in cache):
                return cache[i]

            if(i % 2 == 0):
                cache[i] = 1 + dp(i / 2)
            else:
                cache[i] = 1 + min(dp(i+1), dp(i-1))
            
            return cache[i]

        return dp(n)