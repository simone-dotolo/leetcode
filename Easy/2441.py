class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()

        right = len(nums) - 1
        left = 0

        while left <= right and nums[left] < 0:
            tot = nums[right] + nums[left]
            if tot ==  0:
                return nums[right]
            elif tot > 0:
                right -= 1
            else:
                left += 1
        
        return -1