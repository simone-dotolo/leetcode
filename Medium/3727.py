class Solution:
    def maxAlternatingSum(self, nums: List[int]) -> int:
        n = len(nums)
        nums = sorted(num ** 2 for num in nums)
        return sum(nums[n//2:]) - sum(nums[:n//2]) 
