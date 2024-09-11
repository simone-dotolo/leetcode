class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:

        cache = {}

        nums.sort()

        def dp(nums,i):

            if(i >= len(nums)):
                return 0
            
            if(i in cache):
                return cache[i]

            j = 1

            while(i+j < len(nums) and nums[i+j] == nums[i]):
                j += 1
            
            k = j

            while(i+k < len(nums) and nums[i+k] == nums[i] + 1):
                k += 1

            cache[i] = max(dp(nums,i+j), nums[i] * j + dp(nums,i+k))

            return cache[i]

        return dp(nums,0)