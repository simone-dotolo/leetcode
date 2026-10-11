class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        return sum(nums[index-1] ** 2 for index in [i for i in range(1, len(nums)+1) if len(nums) % i == 0])
