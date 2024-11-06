class Solution:
    def canSortArray(self, nums: List[int]) -> bool:

        def count_set_bit(a):
            count = 0
            while a > 1:
                count += (a % 2)
                a = a // 2
            return count + 1

        def eq_set_bits(a, b):
            return count_set_bit(a) == count_set_bit(b)
        
        def is_sorted(nums):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1]:
                    return False
            return True

        for _ in range(len(nums)):
            for i in range(1, len(nums)):
                if nums[i] < nums[i-1] and eq_set_bits(nums[i], nums[i-1]):
                    nums[i], nums[i-1] = nums[i-1], nums[i]

        return is_sorted(nums)
