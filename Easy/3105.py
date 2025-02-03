class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        max_inc = 1
        curr_inc = 1
        max_dec = 1
        curr_dec = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                curr_inc += 1
                if curr_inc > max_inc:
                    max_inc = curr_inc
            else:
                curr_inc = 1
            if nums[i] < nums[i-1]:
                curr_dec += 1
                if curr_dec > max_dec:
                    max_dec = curr_dec
            else:
                curr_dec = 1
        
        return max(max_inc, max_dec)
