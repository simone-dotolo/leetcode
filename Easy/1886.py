class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        def rotate(mat):
            nrows = len(mat)
            ncols = len(mat[0])
            rotated = [[0 for _ in range(ncols)] for _ in range(nrows)]
            for i in range(nrows):
                for j in range(ncols):
                    rotated[i][j] = mat[j][ncols - i - 1]
            return rotated
        
        def eq(mat1, mat2):
            nrows = len(mat1)
            ncols = len(mat1[0])
            for i in range(nrows):
                for j in range(ncols):
                    if mat1[i][j] != mat2[i][j]:
                        return False
            return True
        
        for _ in range(4):
            mat = rotate(mat)
            if eq(mat, target):
                return True

        return False
