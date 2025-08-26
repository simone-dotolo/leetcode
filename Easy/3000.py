class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        from math import sqrt
        max_area = 0
        max_diag = 0
        for rect in dimensions:
            h, w = rect
            diag = sqrt(h ** 2 + w ** 2)
            if diag > max_diag:
                max_diag = diag
                max_area = h * w
            elif diag == max_diag:
                max_area = max(max_area, h * w)
        return max_area
        
