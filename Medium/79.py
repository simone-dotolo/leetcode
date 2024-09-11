class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        def is_solution(path,target):

            string = ''
            for el in path:
                string += el
            return string == target

        def make_move(board,position,path):
            
            row, col = position
            path.append(board[row][col])
            board[row][col] = None
        
        def unmake_move(board, position,path):
            row,col = position
            letter = path.pop()
            board[row][col] = letter

        def calculate_next_moves(board,position,path,target):

            row, col = position
            curr_letters = len(path)
            moves = []

            if(curr_letters == len(target)):
                return moves

            if(row + 1 < len(board) and (board[row+1][col] == target[curr_letters])):
                moves.append((row+1,col))
            if(col + 1 < len(board[0]) and (board[row][col+1] == target[curr_letters])):
                moves.append((row,col+1))
            if(row - 1 >= 0 and (board[row-1][col] == target[curr_letters])):
                moves.append((row-1,col))
            if(col - 1 >= 0 and (board[row][col-1] == target[curr_letters])):
                moves.append((row,col-1))

            return moves

        def solve(board,position,path,target):

            make_move(board,position,path)
            
            if(is_solution(path,target)):
                return True
            else:
                for next_move in calculate_next_moves(board, position,path, target):
                    solve(board,next_move,path,target)

                    if(is_solution(path,target)):
                        return True

            unmake_move(board, position, path)

        path = []
        for i in range(len(board)):
            for j in range(len(board[0])):
                
                if(board[i][j]==word[0]):
                    if(solve(board, (i,j), path, word)):
                        return True

        return False
