class Solution:
    def totalNQueens(self, n: int) -> int:
        def make_move(board,position,path):

            i,j = position
            board[i][j] = 1
            path.append(position)

        def unmake_move(board,position,path):
            
            i,j = position
            board[i][j] = 0
            path.pop()

        def is_valid(board,position):
            
            i,j = position

            if(sum(board[i]) > 1):
                return False
            
            col = [row[j] for row in board]

            if(sum(col) > 1):
                return False

            diag_sum = board[i][j]

            m = 1
            n = 1

            while(i+m < len(board) and j+n < len(board[0])):
                diag_sum += board[i+m][j+n]
                m += 1
                n += 1

            m = 1
            n = 1

            while(i-m >= 0 and j-n >= 0 ):
                diag_sum += board[i-m][j-n]
                m += 1
                n += 1

            if(diag_sum > 1):
                return False

            diag_sum = board[i][j]

            m = 1
            n = 1

            while(i-m >= 0 and j+n < len(board[0])):
                diag_sum += board[i-m][j+n]
                m += 1
                n += 1

            while(i+m < len(board) and j-n >= 0):
                diag_sum += board[i+m][j-n]
                m += 1
                n += 1

            if(diag_sum > 1):
                return False

            return True
            

        def is_solution(board,path):
            
            return len(path) == len(board)

        def solve(board,position,path,res):


            i,j = position
            
            make_move(board,position,path)

            if(is_valid(board,position) is False):
                unmake_move(board,position,path)
                return

            if(is_solution(board,path)):
                res.append(path.copy())
            else:

                for k in range(len(board[0])):
                    if (k != j and k != j-1 and k != j+1):
                        solve(board,(i+1,k),path,res)

            unmake_move(board,position,path)

            return res

        board = [ 
                [1,2,3,4,5,6,7,8], 
                [9,10,11,12,13,14,15,16], 
                [17,18,19,20,21,22,23,24], 
                [25,26,27,28,29,30,31,32], 
                [33,34,35,36,37,38,39,40], 
                [41,42,43,44,45,46,47,48], 
                [49,50,51,52,53,54,55,56], 
                [57,58,59,60,61,62,63,64] 
                ]

        #n = 9

        board = [ [0 for i in range(n)] for i in range(n)]

        path = []
        res = []
        for i in range(len(board)):
            solve(board,(0,i),path,res)

        return len(res)