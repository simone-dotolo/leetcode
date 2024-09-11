class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cache = {}

        def dp(nums,i):

            if(i == -1):
                return min(dp(nums,i+1),dp(nums,i+2))

            if(i >= len(nums)):
                return 0
            
            if(i in cache):
                return cache[i]
            
            cache[i] = min(nums[i] + dp(nums,i+1), nums[i] + dp(nums,i+2))
        
            return cache[i]
        
        return dp(cost,-1)