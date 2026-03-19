class Solution:
    def numberOfSubmatrices(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                c = grid[i][j]

                if c == 'X':
                    grid[i][j] = 1
                elif c == 'Y':
                    grid[i][j] = 1000000
                else:
                    grid[i][j] = 0
                grid[i][j] += 0 if j - 1 < 0 else grid[i][j - 1]
                grid[i][j] += 0 if i - 1 < 0 else grid[i - 1][j]
                grid[i][j] -= 0 if j - 1 < 0 or i - 1 < 0 else grid[i - 1][j - 1]

                num_x = grid[i][j] % 1000000
                num_y = grid[i][j] // 1000000

                if num_x == num_y and num_x > 0:
                    res += 1
        return res
