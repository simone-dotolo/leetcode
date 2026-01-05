class Solution:
    def maxMatrixSum(self, matrix: List[List[int]]) -> int:
        res = 0
        min_val = float('inf')
        n_neg = 0

        for row in matrix:
            for col in row:
                res += abs(col)
                min_val = min(min_val, abs(col))
                n_neg += int(col < 0)

        return res - 2 * min_val * (n_neg % 2)
