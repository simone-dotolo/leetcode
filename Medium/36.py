class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = 9
        cols = 9

        for i in range(rows):
            row_count = [0 for _ in range(cols)]
            for j in range(cols):
                if board[i][j] != '.':
                    if row_count[(int(board[i][j])) - 1]:
                        return False
                    row_count[int(board[i][j]) - 1] += 1
        
        for j in range(cols):
            col_count = [0 for _ in range(rows)]
            for i in range(rows):
                if board[i][j] != '.':
                    if col_count[(int(board[i][j])) - 1]:
                        return False
                    col_count[int(board[i][j]) - 1] += 1

        for i in range(0, rows, 3):
            for j in range(0, cols, 3):
                block_count = [0 for _ in range(9)]
                block = [row[j:j+3] for row in board[i:i+3]]
                print(block)
                for m in range(3):
                    for n in range(3):
                        if block[m][n] != '.':
                            if block_count[(int(block[m][n])) - 1]:
                                return False
                            block_count[int(block[m][n]) - 1] += 1 
                print(block_count)
        return True

