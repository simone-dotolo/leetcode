class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        def binary_search(nums, el, mode):
            low = 0
            high = len(nums) - 1

            while low <= high:
                mid = low + (high - low) // 2

                if nums[mid] == el:
                    return mid
                elif nums[mid] > el:
                    high = mid - 1
                    if mode == 'upper':
                        mid = high
                else:
                    low = mid + 1
                    if mode == 'lower':
                        mid = low

            return mid

        digits = '123456789'
        nums = []

        for s in range(1, 10):
            for i in range(10 - s):
                nums.append(int(digits[i:i+s]))
        
        low_num = binary_search(nums, low, mode='lower')
        high_num = binary_search(nums, high, mode='upper')

        return nums[low_num:high_num+1]
