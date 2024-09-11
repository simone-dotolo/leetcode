class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:

        cache = {}

        def dp(s, i, j):

            if(i == j):
                return 1
            
            if(i > j):
                return 0
            
            if((i,j) in cache):
                return cache[(i,j)]
            
            l = 0

            if(s[i] == s[j]):
                cache[(i,j)] = 2 + dp(s,i+1,j-1)
                return cache[(i,j)]
            
            cache[(i,j)] = max(dp(s,i+1,j),dp(s,i,j-1))
            return cache[(i,j)]
        
        return dp(s,0,len(s)-1)