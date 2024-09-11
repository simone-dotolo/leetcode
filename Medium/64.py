class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        from math import inf

        cache = {}

        def dp(grid,i,j):

            print(i,j)

            if(i == len(grid)-1 and j == len(grid[0])-1):
                cache[(i,j)] = grid[i][j]
                return cache[(i,j)]

            if(i > len(grid)-1 or j > len(grid[0])-1):
                return inf
            
            if((i,j) in cache):
                return cache[(i,j)]
            
            cache[(i,j)] = grid[i][j] + min(dp(grid,i+1,j),dp(grid,i,j+1))

            return cache[(i,j)]
        
        return dp(grid,0,0)