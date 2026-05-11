class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []
        for num in nums:
            res.extend(int(c) for c in str(num))
        return res
