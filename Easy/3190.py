class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res += int(num % 3 > 0)
        return res
        
