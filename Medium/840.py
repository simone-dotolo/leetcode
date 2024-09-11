class Solution:

    def is_valid(self, matrix):

        if sum([sum(row) for row in matrix]) != 45:
            return 0
        
        numbers = []

        for row in matrix:
            numbers.extend(row)
        
        if set(numbers) != set([1,2,3,4,5,6,7,8,9]):
            return 0
        
        target_sum = sum(matrix[0])

        for row in matrix:
            if sum(row) != target_sum:
                return 0
        
        for i in range(3):
            col = [row[i] for row in matrix]
            if sum(col) != target_sum:
                return 0
        
        diag1 = [matrix[i][i] for i in range(3)]
        diag2 = [matrix[-i][-i] for i in range(1,4)]

        if sum(diag1) != target_sum or sum(diag2) != target_sum:
            return 0

        return 1

        

    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        
        if len(grid) < 3 or len(grid[0]) < 3:
            return 0
        
        if len(grid) == 3 and len(grid[0]) == 3:
            return self.is_valid(grid)

        magic_squares_count = 0

        for row in range(len(grid)-2):
            rows = grid[row:row+3]
            for col in range(len(grid[0])-2):
                submatrix = [el[col:col+3] for el in rows]
                magic_squares_count += self.is_valid(submatrix)
        
        return magic_squares_count