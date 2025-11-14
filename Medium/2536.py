class Solution:
    def rangeAddQueries(self, n: int, queries: List[List[int]]) -> List[List[int]]:
        integral_matrix = [[0 for _ in range(n)] for _ in range(n)]

        # Submatrix with top-left p1 (x1;y1) and bottom-right p2(x2;y2) is equivalent
        # to the sum of 4 submatrices with top-left corner (0;0)
        # S1 = S2 + S3 - S4 - S5
        # S2 has bottom-right (x2;y2)
        # S3 has bottom-right (x1-1;y1-1)
        # S4 has bottom-right (x1-1;y2)
        # S5 has bottom-right (x2;y1-1)
        # Time complexity: O(q)
        # Space complexity: O(n^2)
        for query in queries:
            x1, y1, x2, y2 = query
            integral_matrix[x2][y2] += 1
            if x1 >= 1:
                integral_matrix[x1 - 1][y2] -= 1
            if y1 >= 1:
                integral_matrix[x2][y1 - 1] -= 1
            if x1 >= 1 and y1 >= 1:
                integral_matrix[x1 - 1][y1 - 1] += 1

      # Convert integral_matrix into res (bottom_up)
        res = [[0 for _ in range(n)] for _ in range(n)]
        curr = 0

        # Compute bottom-row
        for j in range(n - 1, -1, -1):
            if integral_matrix[-1][j]:
                curr += integral_matrix[-1][j]
            res[-1][j] = curr

        # O(n^2)
        # Each element is below(element) + curr
        for i in range(n - 2, -1, -1):
            curr = 0
            for j in range(n - 1, -1, -1):
                if integral_matrix[i][j]:
                    curr += integral_matrix[i][j]
                res[i][j] = res[i + 1][j] + curr

        # Time complexity: O(q + n^2)
        # Space complexity: O(n^2)
        return res
