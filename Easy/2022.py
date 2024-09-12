class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != (m * n):
            return []
        
        res = [[0] * n for _ in range(m)]

        for i, el in enumerate(original):
            row = i // n
            col = i % n
            res[row][col] = el
        
        return res
