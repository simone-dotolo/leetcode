class Solution:
    def areSimilar(self, mat: List[List[int]], k: int) -> bool:
        def eq_shifted(row, start):
            n = len(row)
            for i in range(n):
                if row[i] != row[(start+i)%n]:
                    return False
            return True

        n = len(mat[0])

        for i, row in enumerate(mat):
            start = k if i % 2 == 0 else n - k
            if not eq_shifted(row, start):
                return False
        
        return True
