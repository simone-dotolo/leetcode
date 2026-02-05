class Solution:
    def constructTransformedArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        result = [0 for _ in range(n)]

        for i, num in enumerate(nums):
            if num == 0:
                result[i] = num
            else:
                result[i] = nums[(i + nums[i]) % n]
        
        return result
        
