class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:

        if(len(nums) == 1):
            return True

        cache = {}

        def dp(nums,i,j):

            if(i > j):
                return 0
            
            if((i,j) in cache):
                return cache[(i,j)]

            cache[(i,j)] = max(nums[i] + min(dp(nums,i+1,j-1),dp(nums,i+2,j)), nums[j] + min(dp(nums,i+1,j-1), dp(nums,i,j-2)))

            return cache[(i,j)]
        
        return 2*(dp(nums,0,len(nums)-1)) >= sum(nums)