class Solution:
    def isTrionic(self, nums: List[int]) -> bool:
        if len(nums) == 3:
            return False

        peaks = 0
        for i in range(1, len(nums) - 1):
            if nums[i] == nums[i - 1]:
                return False
            if ((nums[i] > nums[i-1]) and (nums[i] > nums[i+1])):
                peaks += 1
        peaks += 2

        return peaks == 3 and nums[1] > nums[0] and nums[-2] < nums[-1] 
