class Solution:
    def minMoves(self, nums: list[int]) -> int:
        res = 0
        min_num = min(nums)
        for num in nums:
            res += (num - min_num)
        return res
