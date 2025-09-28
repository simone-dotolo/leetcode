class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()

        def perimeter(s1, s2, s3):
            if (s1 < s2 + s3) and (s2 < s1 + s3) and (s3 < s1 + s2):
                return s1 + s2 + s3
            return 0

        n = len(nums)
        max_perimeter = 0

        for i in range(n - 2):
            max_perimeter = max(max_perimeter, perimeter(nums[i], nums[i + 1], nums[i + 2]))
        
        return max_perimeter
