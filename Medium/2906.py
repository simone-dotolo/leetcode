class Solution:
    def constructProductMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        nrows = len(grid)
        ncols = len(grid[0])

        res1 = [[1 for _ in range(ncols)] for _ in range(nrows)]

        for i in range(nrows):
            for j in range(ncols):
                if j > 0:
                    res1[i][j] = grid[i][j-1] * res1[i][j-1] % 12345
                elif i > 0:
                    res1[i][j] = grid[i-1][-1] * res1[i-1][-1] % 12345
        
        res2 = [[1 for _ in range(ncols)] for _ in range(nrows)]
        for i in range(nrows - 1, -1, -1):
            for j in range(ncols - 1, -1, -1):
                if j < ncols - 1:
                    res2[i][j] = grid[i][j+1] * res2[i][j+1] % 12345
                elif i < nrows - 1:
                    res2[i][j] = grid[i+1][0] * res2[i+1][0] % 12345

        for i in range(nrows):
            for j in range(ncols):
                res1[i][j] = res1[i][j] * res2[i][j] % 12345
        
        return res1
