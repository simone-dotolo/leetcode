class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        for i,row in enumerate(grid):
            if row[0] == 0:
                grid[i] = [el^1 for el in row]
        
        rows = len(grid)
        cols = len(grid[0])

        for i in range(1,cols):
            col = [row[i] for row in grid]
            if sum(col) <= (rows//2):
                col = [el^1 for el in col]
                for j in range(rows):
                    grid[j][i] = col[j]

        ans = 0
        for row in grid:
            for j in range(cols):
                ans += (2**(cols - 1 - j) * row[j])
        
        return ans