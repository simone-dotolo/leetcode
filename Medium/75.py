class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        freq = [0 for _ in range(3)]

        for num in nums:
            freq[num] += 1
                
        curr_pos = 0
        curr_num = 0
        while curr_pos < len(nums):
            if curr_pos < sum(freq[:curr_num+1]):
                nums[curr_pos] = curr_num
            elif curr_pos < sum(freq[:curr_num+2]):
                curr_num += 1
                nums[curr_pos] = curr_num
            else:
                curr_num += 2
                nums[curr_pos] = curr_num
            curr_pos += 1
        
        return nums