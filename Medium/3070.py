class Solution(object):
    def countSubmatrices(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: int
        """
        rows = len(grid)
        cols = len(grid[0])
        res = 0

        for i in range(rows):
            for j in range(cols):
                grid[i][j] += 0 if j - 1 < 0 else grid[i][j - 1]
                grid[i][j] += 0 if i - 1 < 0 else grid[i - 1][j]
                grid[i][j] -= 0 if j - 1 < 0 or i - 1 < 0 else grid[i - 1][j - 1]

                if grid[i][j] <= k:
                    res += 1
        return res
