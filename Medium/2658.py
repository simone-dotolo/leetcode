class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        def dfs(i, j):
            if (i < 0) or (i > len(grid) - 1) or (j < 0) or (j > len(grid[0]) - 1) or (grid[i][j] == 0):
                return 0
            res = grid[i][j]
            grid[i][j] = 0
            res += (dfs(i+1,j) + dfs(i-1,j) + dfs(i,j-1) + dfs(i,j+1))
            return res
        
        res = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                res = max(res, dfs(i,j))
        
        return res
