class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        res = float('inf')
        for i in range(k - 1, len(nums)):
            res = min(res, abs(nums[i] - nums[i - k + 1]))
        return res
