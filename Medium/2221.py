class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i, num in enumerate(nums):
            res += int(num * factorial(n - 1) // (factorial(n - 1 - i) * factorial(i))) % 10
        return res % 10
