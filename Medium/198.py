class Solution:
    def rob(self, nums: List[int]) -> int:

        if(len(nums) == 1):
            return nums[0]

        r = [0] * len(nums)

        r[0] = nums[0]
        r[1] = max(nums[0],nums[1])

        for i in range(2,len(r)):
            r[i] = max(r[i-1], r[i-2] + nums[i])

        return max(r)