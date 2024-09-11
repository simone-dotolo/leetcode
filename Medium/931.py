class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:

        from math import inf

        cache = {}

        def dp(i,j):

            if(i == -1):
                return min([dp(0,k) for k in range(len(matrix[0]))])

            if(i >= len(matrix)):
                return 0
            
            if(j >= len(matrix[0]) or j < 0):
                return inf

            if((i,j) in cache):
                return cache[(i,j)]

            cache[(i,j)] = matrix[i][j] + min(dp(i+1,j-1), dp(i+1,j), dp(i+1,j+1))

            return cache[(i,j)]
        
        return dp(-1,0)