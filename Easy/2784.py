class Solution:
    def isGood(self, nums: List[int]) -> bool:
        return len(set(nums)) == len(nums) - 1 and (sum(nums) - max(nums)) == (len(set(nums)) * (len(set(nums)) + 1)) // 2
