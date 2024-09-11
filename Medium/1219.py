class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        
        nrows = len(grid)
        ncols = len(grid[0])
        res = 0

        def solve(row, col, curr_sum):
            if row < 0 or row >= nrows or col < 0 or col >= ncols:
                return curr_sum

            if grid[row][col] == 0:
                return curr_sum
            
            gold = grid[row][col]
            curr_sum += gold
            grid[row][col] = 0

            curr_sum = max(solve(row-1, col, curr_sum),
            solve(row+1, col, curr_sum),
            solve(row, col-1, curr_sum),
            solve(row, col+1, curr_sum)
            )

            grid[row][col] = gold

            return curr_sum


        
        for i in range(nrows):
            for j in range(ncols):
                if grid[i][j] != 0:
                    res = max(res, solve(i, j, 0))
        
        return res