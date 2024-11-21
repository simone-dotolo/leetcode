from typing import List

class Solution:

    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        def explore_north(grid, row, col):
            upward_row = row - 1
            counter = 0
            while upward_row >= 0 and grid[upward_row][col] != 3 and grid[upward_row][col] != 2:
                if grid[upward_row][col] == 0:
                    grid[upward_row][col] = 1
                    counter += 1
                upward_row -= 1
            return counter
        
        def explore_south(grid, row, col):
            downward_row = row + 1
            counter = 0
            while downward_row < len(grid) and grid[downward_row][col] != 3 and grid[downward_row][col] != 2:
                if grid[downward_row][col] == 0:
                    grid[downward_row][col] = 1
                    counter += 1
                downward_row += 1
            return counter
    
        def explore_west(grid, row, col):
            left_col = col - 1
            counter = 0
            while left_col >= 0 and grid[row][left_col] != 3 and grid[row][left_col] != 2:
                if grid[row][left_col] == 0:
                    grid[row][left_col] = 1
                    counter += 1
                left_col -= 1
            return counter
        
        def explore_east(grid, row, col):
            right_col = col + 1
            counter = 0
            while right_col < len(grid[0]) and grid[row][right_col] != 3 and grid[row][right_col] != 2:
                if grid[row][right_col] == 0:
                    grid[row][right_col] = 1
                    counter += 1
                right_col += 1
            return counter
    
        grid = [[0] * n for _ in range(m)]

        res = m * n

        for wall in walls:
            row, col = wall
            grid[row][col] = 3
            res -= 1


        for guard in guards:
            row, col = guard
            grid[row][col] = 2
            res -= 1

        for guard in guards:
            row, col = guard
            res -= explore_north(grid, row, col)
            res -= explore_south(grid, row, col)
            res -= explore_east(grid, row, col)
            res -= explore_west(grid, row, col)

        return res, grid
    
test = Solution()
res, grid = test.countUnguarded(m = 4, n = 6, guards = [[0,0],[1,1],[2,3]], walls = [[0,1],[2,2],[1,4]])

print(res)
for row in grid:
    print(*row)

res, grid = test.countUnguarded(m = 3, n = 3, guards = [[1,1]], walls = [[0,1],[1,0],[2,1],[1,2]])

print(res)
for row in grid:
    print(*row)

res, grid = test.countUnguarded(m = 2, n = 7, guards = [[1,5],[1,1],[1,6],[0,2]], walls = [[0,6],[0,3],[0,5]])

print(res)
for row in grid:
    print(*row)