class Solution:
    def countPartitions(self, nums: List[int]) -> int:
        res = 0
        diff = nums[0] - sum(nums[1:])

        if diff % 2 == 0:
            res += 1

        for num in nums[1:-1]:
            diff += (2 * num)
            if diff % 2 == 0:
                res += 1
        
        return res
