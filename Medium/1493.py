class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        arr = []
        i = 0
        while i < len(nums):
            if nums[i] == 0:
                arr.append(nums[i])
                i += 1
            else:
                j = 0
                while i + j < len(nums) and nums[i+j]:
                    j += 1
                i += j
                arr.append(j)
        
        if len(arr) == 1:
            return arr[0] - nums[0]
        elif len(arr) == 2:
            return max(arr)

        res = 0
        for i in range(len(arr) - 2):
            if sum(arr[i:i+3]) > res:
                res = sum(arr[i:i+3])
        
        return res
