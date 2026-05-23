class Solution:
    def check(self, nums: List[int]) -> bool:
        start = nums[0]
        dec = 0
        
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                dec += 1
        
        if dec > 1 or dec == 1 and nums[-1] > start:
            return False
        
        return True
