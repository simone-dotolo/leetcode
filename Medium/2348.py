class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        res = 0
        curr_length = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                res += (curr_length + 1)
                curr_length += 1
            else:
                curr_length = 0
        return res
        
