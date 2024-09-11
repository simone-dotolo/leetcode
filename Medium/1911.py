class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:

        cache = {}

        def dp(nums, i, even):

            if(i >= len(nums)):
                return 0

            if((i,even) in cache):
                return cache[(i,even)]
            
            if(even is True):
                cache[(i,even)] = max(nums[i] + dp(nums,i+1,False), dp(nums,i+1,True))
            else:
                cache[(i,even)] = max(-nums[i] + dp(nums,i+1,True), dp(nums,i+1,False))

            return cache[(i,even)]
        
        return dp(nums,0,True)