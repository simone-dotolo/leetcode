class Solution:
    def numSpecial(self, mat: List[List[int]]) -> int:
        def add_rows(row1, row2):
            return [el1 + el2 for el1, el2 in zip(row1, row2)]

        mask = [0 for _ in range(len(mat[0]))]

        for row in mat:
            mask = add_rows(row, mask)
        
        mask = int(''.join([str(int(el == 1)) for el in mask]), 2)

        rows = [int(''.join([str(el) for el in row]), 2) for row in mat]

        res = 0

        for row in rows:
            masked_row = row & mask
            if masked_row and row & (row - 1) == 0:
                res += 1

        return res
