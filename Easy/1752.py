class Solution:
    def check(self, nums: List[int]) -> bool:
        min_index = 0
        min_value = nums[0]
        for i in range(1,len(nums)):
            if nums[i] <= min_value and nums[i-1] != nums[i]:
                min_value = nums[i]
                min_index = i
        
        for i in range(1,len(nums)):
            index = (min_index + i) % len(nums)
            if nums[index] < nums[index - 1]:
                return False
        return True
