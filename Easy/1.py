class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        new_nums = sorted(nums)

        first, second = 0, 0
        first_index, second_index = 0, 0
        
        i = 0
        while i < len(new_nums):
            num = new_nums[i]
            new_target = target - num
            # Binary search of new_target in nums
            low = i+1
            high = len(new_nums) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if new_nums[mid] == new_target:
                    low = high + 1
                    i = len(new_nums) + 1
                    first, second = num, new_nums[mid]
                elif new_nums[mid] > new_target:
                    high = mid - 1
                else:
                    low = mid + 1
            i += 1

        i = 0
        while i < len(nums):
            if nums[i] == first:
                first_index = i
                i = len(nums) + 1
            i += 1
        
        i = 0
        while i < len(nums):
            if nums[i] == second and i != first_index:
                second_index = i
                i = len(nums) + 1
            i += 1
    
        return first_index, second_index