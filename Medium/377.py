class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:

        cache = {}

        def dp(nums, i, curr_sum):

            if(i >= len(nums)):
                return 0

            if((i,curr_sum) in cache):
                return cache[(i,curr_sum)]

            if(nums[i] + curr_sum == target):
                cache[(i,curr_sum)] = 1 + dp(nums,i+1,curr_sum)
                return cache[(i,curr_sum)]

            if(nums[i] + curr_sum > target):
                cache[(i,curr_sum)] = dp(nums,i+1,curr_sum)
                return cache[(i,curr_sum)]

            cache[(i,curr_sum)] = dp(nums,i+1,curr_sum) + dp(nums,0,curr_sum+nums[i])

            return cache[(i,curr_sum)]

        return dp(nums,0,0)