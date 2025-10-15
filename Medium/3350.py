class Solution:
    def maxIncreasingSubarrays(self, nums: List[int]) -> int:
        res = 1
        prev = 0
        curr = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                curr += 1
            else:
                res = max(res, min(curr, prev), curr // 2)
                prev = curr
                curr = 1
                
        res = max(res, min(curr, prev), curr // 2)

        return res
