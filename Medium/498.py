class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        rows = len(mat)
        cols = len(mat[0])

        res = []
        rev = False
        for i in range(rows):
            j = 0
            curr_diag = []
            while i >= 0 and j < cols:
                curr_diag.append(mat[i][j])
                i -= 1
                j += 1
            if rev:
                res.extend(curr_diag[::-1])
            else:
                res.extend(curr_diag)
            rev = not rev
        
        for j in range(1, cols):
            i = rows - 1
            curr_diag = []
            while i >= 0 and j < cols:
                curr_diag.append(mat[i][j])
                i -= 1
                j += 1
            if rev:
                res.extend(curr_diag[::-1])
            else:
                res.extend(curr_diag)
            rev = not rev
    
        return res
        
