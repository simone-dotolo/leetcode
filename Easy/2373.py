class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        rows = len(grid)
        cols = len(grid[0])
        ans = []

        for i in range(rows - 2):
            for j in range(cols - 2):
                tmp = []
                submatrix = [row[j:j+3] for row in grid[i:i+3]]
                for row in submatrix:
                    for col in row:
                        tmp.append(col)
                ans.append(max(tmp))
        
        ans = [ans[i*(cols-2):i*(cols-2) + cols-2] for i in range(rows-2)]

        return ans