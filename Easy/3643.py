class Solution:
    def reverseSubmatrix(self, grid: List[List[int]], x: int, y: int, k: int) -> List[List[int]]:
        for count, i in enumerate(range(x, x + k // 2)):
            for j in range(y, y + k):
                grid[i][j], grid[x + k - count - 1][j] = grid[x + k - count - 1][j], grid[i][j] 
        return grid
        
