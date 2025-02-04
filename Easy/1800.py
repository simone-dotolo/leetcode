class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > nums[i-1]:
                curr_sum += nums[i]
                if curr_sum > max_sum:
                    max_sum = curr_sum
            else:
                curr_sum = nums[i]
        return max_sum
