class Solution:
    def countSubarrays(self, nums: List[int]) -> int:

        ans = 0
        for i in range(len(nums) - 2):
            ans += int((2 * (nums[i] + nums[i+2])) == nums[i+1])
        return ans
