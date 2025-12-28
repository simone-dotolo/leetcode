class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        def find_first_negative(row):
            left = 0
            right = len(row) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if row[mid] >= 0:
                    left = mid + 1
                else:
                    right = mid - 1
                    index = mid
            
            return index

        n = len(grid[0])
        res = 0
        for row in grid:
            index = find_first_negative(row)
            res += (n - index) if index != -1 else 0
        
        return res
