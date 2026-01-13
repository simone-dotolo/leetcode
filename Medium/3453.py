class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        def compute_area(squares, y):
            curr_area = 0
            for square in squares:
                if square[1] <= y:
                    base = square[2]
                    height = square[2] if (square[1] + square[2]) < y else (y - square[1])
                    curr_area += base * height
            return curr_area

        total_area = 0
        min_y = float('inf')
        max_y = float('-inf')

        for square in squares:
            total_area += square[2] ** 2
            min_y = min(min_y, square[1])
            max_y = max(max_y, square[1] + square[2])

        left = min_y
        right = max_y
        
        target_area = total_area / 2
        
        while abs(left - right) > 1e-5:
            mid = (left + right) / 2
            area = compute_area(squares, mid)

            if area < target_area:
                left = mid
            else:
                right = mid

        return mid
