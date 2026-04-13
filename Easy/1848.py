class Solution(object):
    def getMinDistance(self, nums, target, start):
        """
        :type nums: List[int]
        :type target: int
        :type start: int
        :rtype: int
        """
        return min(abs(i - start) if el == target else float('inf') for i, el in enumerate(nums))
