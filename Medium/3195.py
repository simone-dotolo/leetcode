class Solution:
    def minimumArea(self, grid: List[List[int]]) -> int:
        min_row, min_col = 1000, 1000
        max_row, max_col = -1, -1

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    min_row = min(min_row, i)
                    max_row = max(max_row, i)
                    min_col = min(min_col, j)
                    max_col = max(max_col, j)
        
        return (max_row - min_row + 1) * (max_col - min_col + 1)
