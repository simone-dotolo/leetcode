class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        max_nums = max(nums)
        ans = 0
        left = 0
        curr_count = 0

        for right in range(len(nums)):
            if nums[right] == max_nums:
                curr_count += 1
            
            while curr_count == k:
                ans += (len(nums) - right)
                if nums[left] == max_nums:
                    curr_count -= 1
                left += 1
                
        return ans
