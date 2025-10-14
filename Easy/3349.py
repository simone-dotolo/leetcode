class Solution:
    def hasIncreasingSubarrays(self, nums: List[int], k: int) -> bool:
        def strictly_inc(arr):
            for i in range(1, len(arr)):
                if arr[i] <= arr[i - 1]:
                    return False
            return True
        
        for i in range(len(nums) - 2 * k + 1):
            if strictly_inc(nums[i:i+k]) and strictly_inc(nums[i+k:i+2*k]):
                return True
        return False
