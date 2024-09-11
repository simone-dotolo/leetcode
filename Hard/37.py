class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def find_empty(bo):

            for i in range(len(bo)):
                for j in range(len(bo[0])):
                    if bo[i][j] == 0:
                        return (i,j)

            return None

        def valid(bo, num, position):

            row, col = position

            for i in range(len(bo)):
                if(bo[row][i] == num and i != col):
                    return False

            for i in range(len(bo[0])):
                if(bo[i][col] == num and i != row):
                    return False

            cell_row = row // 3
            cell_col =  col // 3

            for i in range(cell_row * 3, (cell_row + 1) * 3):
                for j in range(cell_col * 3, (cell_col + 1) * 3):
                    if(bo[i][j] == num and i != row and j != col):
                        return False

            return True

        def solve(bo):

            position = find_empty(bo)

            if(position == None):
                return bo

            row, col = position

            for i in range(1,10):
                if(valid(bo, i, (row,col))):
                    bo[row][col] = i

                    if(solve(bo)):
                        return bo

                    bo[row][col] = 0

            return None
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j] != '.'):
                    board[i][j] = int(board[i][j])
                else:
                    board[i][j] = 0
        
        board = solve(board)
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                    board[i][j] = str(board[i][j])