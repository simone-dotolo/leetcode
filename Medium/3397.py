class Solution:
    def maxDistinctElements(self, nums: List[int], k: int) -> int:
        # O(nlogn), sort and make every elements the smallest possible
        nums.sort()
        nums[0] -= k
      
        for i in range(1, len(nums)):
            nums[i] = min(max(nums[i-1] + 1, nums[i] - k), nums[i] + k)

        return len(set(nums))
