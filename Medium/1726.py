class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import Counter
        ans = 0
        count = Counter()
        for i in range(len(nums)):
            for j in range(i):
                prod = nums[i] * nums[j]
                ans += count[prod] * 8
                count[prod] += 1
        return ans
