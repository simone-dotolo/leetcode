class Solution(object):
    def prefixesDivBy5(self, nums):
        """
        :type nums: List[int]
        :rtype: List[bool]
        """
        ans = []

        curr = 0
        for num in nums:
            curr = (curr << 1) + int(num)
            ans.append(curr % 5 == 0)
        return ans
