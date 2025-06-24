class Solution:
    def findKDistantIndices(self, nums: List[int], key: int, k: int) -> List[int]:
        hits = set()
        for i in range(len(nums)):
            if nums[i] == key:
                for j in range(max(0, i - k), min(i + k, len(nums) - 1) + 1):
                    hits.add(j)
        return list(hits)
