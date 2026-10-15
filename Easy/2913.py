class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        res = 0
        n = len(nums)
        for i in range(n):
            curr_set = set()
            for j in range(i, n):
                curr_set.add(nums[j])
                res += len(curr_set) ** 2
        return res
