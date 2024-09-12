class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        cache = {}
        n_rows = len(obstacleGrid)
        n_cols = len(obstacleGrid[0])
        
        def dp(i, j):

            if i >= n_rows or j >= n_cols or obstacleGrid[i][j] == 1:
                return 0
            
            if (i, j) in cache:
                return cache[(i, j)]
            
            found = (i == n_rows - 1) and (j == n_cols - 1)

            cache[(i, j)] = found + dp(i+1, j) + dp(i, j+1)

            return cache[(i, j)]
        
        return dp(0, 0)
