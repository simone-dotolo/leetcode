class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j]:
                    adj = 0
                    if i - 1 >= 0:
                        adj += grid[i-1][j]
                    if j - 1 >= 0:
                        adj += grid[i][j-1]
                    if i + 1 < rows:
                        adj += grid[i+1][j]
                    if j + 1 < cols:
                        adj += grid[i][j+1]
                    res += (4 - adj)
        
        return res