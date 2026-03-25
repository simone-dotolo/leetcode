class Solution(object):
    def canPartitionGrid(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: bool
        """
        nrows = len(grid)
        ncols = len(grid[0])

        target = 0
        for i in range(nrows):
            for j in range(ncols):
                target += grid[i][j]

        target = target / 2.0

        curr = 0
        for i in range(nrows):
            for j in range(ncols):
                curr += grid[i][j]
                if curr == target and j == ncols - 1:
                    return True

        curr = 0
        for j in range(ncols):
            for i in range(nrows):
                curr += grid[i][j]
                if curr == target and i == nrows - 1:
                    return True

        return False
