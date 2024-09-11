class Solution:
    def numDistinct(self, s: str, t: str) -> int:

        cache = {}

        def dp(s,i,j):

            if(i >= len(s) or j >= len(t)):
                return 0

            if((i,j) in cache):
                return cache[(i,j)]

            if(j == len(t) - 1 and s[i] == t[j]):
                cache[(i,j)] = 1 + dp(s,i+1,j)
                return cache[(i,j)]
            
            if(s[i] == t[j]):
                cache[(i,j)] = dp(s,i+1,j) + dp(s,i+1,j+1)
            else:
                cache[(i,j)] = dp(s,i+1,j)
            
            return cache[(i,j)]
        
        return dp(s,0,0)