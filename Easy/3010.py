class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        # Could be O(n) keeping track of the two mins
        return nums[0] + sum(sorted(nums[1:])[:2])
