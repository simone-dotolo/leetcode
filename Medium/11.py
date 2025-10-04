class Solution:
    def compute_area(self, left, right, height):
        return (right - left) * min(height[left], height[right])

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        area = 0

        while left <= right:
            area = max(area, self.compute_area(left, right, height))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return area
