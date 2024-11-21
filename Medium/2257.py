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

        return res
